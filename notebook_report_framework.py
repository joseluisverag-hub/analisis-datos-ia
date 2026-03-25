from __future__ import annotations

import argparse
import base64
import json
import re
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any, Dict, List


TITLE_TAGS = {"title", "report-title"}
INSIGHT_TAGS = {"insight", "finding", "hallazgo"}
CONCLUSION_TAGS = {"conclusion", "conclusiones", "summary", "closing"}
CHART_TAGS = {"chart", "plot", "figure", "grafico", "gráfico"}


@dataclass
class ExtractedChart:
    source_cell_index: int
    output_index: int
    filename: str
    caption: str = ""


@dataclass
class NotebookReport:
    notebook_path: str
    title: str
    insights: List[str]
    conclusion: str
    charts: List[ExtractedChart]
    metadata: Dict[str, Any]


class NotebookReportExtractor:
    TITLE_PATTERNS = [
        re.compile(r"^\s*#\s+(.+)$", re.MULTILINE),
    ]

    INSIGHT_HEADER_PATTERN = re.compile(
        r"^\s{0,3}#{1,6}\s*(insight|hallazgo|hallazgos|finding|findings)\b.*$",
        re.IGNORECASE | re.MULTILINE,
    )

    CONCLUSION_HEADER_PATTERN = re.compile(
        r"^\s{0,3}#{1,6}\s*(conclusi[oó]n|conclusiones|conclusion|summary|resumen final|cierre)\b.*$",
        re.IGNORECASE | re.MULTILINE,
    )

    def __init__(self, notebook_path: str | Path):
        self.notebook_path = Path(notebook_path)
        if not self.notebook_path.exists():
            raise FileNotFoundError(f"No existe el notebook: {self.notebook_path}")

        with self.notebook_path.open("r", encoding="utf-8") as f:
            self.nb = json.load(f)

        self.cells = self.nb.get("cells", [])
        self.nb_metadata = self.nb.get("metadata", {})

    def extract(self, output_dir: str | Path) -> NotebookReport:
        output_dir = Path(output_dir)
        charts_dir = output_dir / "charts"
        charts_dir.mkdir(parents=True, exist_ok=True)

        title = self._extract_title()
        insights = self._extract_insights()
        conclusion = self._extract_conclusion()
        charts = self._extract_charts(charts_dir)

        report = NotebookReport(
            notebook_path=str(self.notebook_path),
            title=title,
            insights=insights,
            conclusion=conclusion,
            charts=charts,
            metadata={
                "kernel": self.nb_metadata.get("kernelspec", {}),
                "language_info": self.nb_metadata.get("language_info", {}),
                "cell_count": len(self.cells),
            },
        )

        manifest_path = output_dir / "report_manifest.json"
        with manifest_path.open("w", encoding="utf-8") as f:
            json.dump(asdict(report), f, indent=2, ensure_ascii=False)

        md_path = output_dir / "report_extracted.md"
        md_lines = [f"# {report.title}", ""]
        if report.insights:
            md_lines += ["## Insights", ""]
            for idx, insight in enumerate(report.insights, 1):
                md_lines += [f"{idx}. {insight}", ""]
        if report.conclusion:
            md_lines += ["## Conclusión", "", report.conclusion, ""]
        if report.charts:
            md_lines += ["## Gráficos extraídos", ""]
            for chart in report.charts:
                line = f"- {chart.filename} (celda {chart.source_cell_index})"
                if chart.caption:
                    line += f" — {chart.caption}"
                md_lines += [line, ""]
        md_path.write_text("\n".join(md_lines), encoding="utf-8")

        return report

    def _cell_source_text(self, cell: Dict[str, Any]) -> str:
        src = cell.get("source", "")
        return "".join(src) if isinstance(src, list) else str(src)

    def _cell_tags(self, cell: Dict[str, Any]) -> set[str]:
        md = cell.get("metadata", {}) or {}
        tags = md.get("tags", []) or []
        return {str(t).strip().lower() for t in tags}

    def _strip_markdown(self, text: str) -> str:
        text = re.sub(r"^\s{0,3}#{1,6}\s*", "", text, flags=re.MULTILINE)
        text = re.sub(r"`{1,3}", "", text)
        text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)
        text = re.sub(r"\*(.*?)\*", r"\1", text)
        text = re.sub(r"!\[.*?\]\(.*?\)", "", text)
        text = re.sub(r"\[(.*?)\]\(.*?\)", r"\1", text)
        lines = [ln.strip() for ln in text.splitlines()]
        lines = [ln for ln in lines if ln]
        return " ".join(lines).strip()

    def _extract_title(self) -> str:
        for cell in self.cells:
            if cell.get("cell_type") == "markdown" and self._cell_tags(cell) & TITLE_TAGS:
                clean = self._strip_markdown(self._cell_source_text(cell))
                if clean:
                    return clean
        for cell in self.cells:
            if cell.get("cell_type") != "markdown":
                continue
            text = self._cell_source_text(cell)
            for patt in self.TITLE_PATTERNS:
                m = patt.search(text)
                if m:
                    return m.group(1).strip()
        return self.notebook_path.stem.replace("_", " ").strip()

    def _extract_insights(self) -> List[str]:
        insights: List[str] = []
        for cell in self.cells:
            if cell.get("cell_type") != "markdown":
                continue
            text = self._cell_source_text(cell)
            tags = self._cell_tags(cell)
            if tags & INSIGHT_TAGS:
                clean = self._strip_markdown(text)
                if clean:
                    insights.append(clean)
                    continue
            if self.INSIGHT_HEADER_PATTERN.search(text):
                clean = self._strip_markdown(text)
                if clean:
                    insights.append(clean)
        deduped, seen = [], set()
        for ins in insights:
            key = ins.lower()
            if key not in seen:
                deduped.append(ins)
                seen.add(key)
        return deduped

    def _extract_conclusion(self) -> str:
        tagged_candidates = []
        header_candidates = []
        for cell in self.cells:
            if cell.get("cell_type") != "markdown":
                continue
            text = self._cell_source_text(cell)
            tags = self._cell_tags(cell)
            if tags & CONCLUSION_TAGS:
                clean = self._strip_markdown(text)
                if clean:
                    tagged_candidates.append(clean)
            if self.CONCLUSION_HEADER_PATTERN.search(text):
                clean = self._strip_markdown(text)
                if clean:
                    header_candidates.append(clean)
        if tagged_candidates:
            return tagged_candidates[-1]
        if header_candidates:
            return header_candidates[-1]
        return ""

    def _infer_chart_caption(self, cell_idx: int) -> str:
        neighbors = []
        if cell_idx - 1 >= 0:
            neighbors.append(self.cells[cell_idx - 1])
        if cell_idx + 1 < len(self.cells):
            neighbors.append(self.cells[cell_idx + 1])
        for cell in neighbors:
            if cell.get("cell_type") != "markdown":
                continue
            text = self._cell_source_text(cell).strip()
            lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
            if not lines:
                continue
            first = re.sub(r"^\s{0,3}#{1,6}\s*", "", lines[0]).strip()
            if 0 < len(first) <= 100:
                return first
        return ""

    def _extract_charts(self, charts_dir: Path) -> List[ExtractedChart]:
        charts: List[ExtractedChart] = []
        chart_counter = 1
        for cell_idx, cell in enumerate(self.cells):
            if cell.get("cell_type") != "code":
                continue
            outputs = cell.get("outputs", [])
            tags = self._cell_tags(cell)
            has_chart_tag = bool(tags & CHART_TAGS)
            for out_idx, output in enumerate(outputs):
                data = output.get("data", {})
                if "image/png" not in data:
                    continue
                b64data = data["image/png"]
                if isinstance(b64data, list):
                    b64data = "".join(b64data)
                try:
                    img_bytes = base64.b64decode(b64data)
                except Exception:
                    continue
                filename = f"chart_{chart_counter:02d}.png"
                file_path = charts_dir / filename
                file_path.write_bytes(img_bytes)
                caption = self._infer_chart_caption(cell_idx)
                if has_chart_tag and not caption:
                    caption = f"Chart extracted from tagged cell {cell_idx}"
                charts.append(
                    ExtractedChart(
                        source_cell_index=cell_idx,
                        output_index=out_idx,
                        filename=str(file_path.name),
                        caption=caption,
                    )
                )
                chart_counter += 1
        return charts


def main() -> None:
    parser = argparse.ArgumentParser(description="Extrae título, gráficos, insights y conclusión desde un notebook.")
    parser.add_argument("notebook", help="Ruta al archivo .ipynb")
    parser.add_argument("--output-dir", default="notebook_report_output", help="Carpeta de salida para charts y manifest")
    args = parser.parse_args()

    extractor = NotebookReportExtractor(args.notebook)
    report = extractor.extract(args.output_dir)

    print("Extracción completada.")
    print(f"Título: {report.title}")
    print(f"Insights extraídos: {len(report.insights)}")
    print(f"Conclusión encontrada: {'sí' if report.conclusion else 'no'}")
    print(f"Gráficos extraídos: {len(report.charts)}")
    print(f"Salida: {Path(args.output_dir).resolve()}")


if __name__ == "__main__":
    main()
