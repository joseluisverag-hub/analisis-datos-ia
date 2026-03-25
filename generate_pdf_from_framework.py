from __future__ import annotations

import json
import os
import sys
from pathlib import Path
from typing import Any, Dict, List

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak


def load_json(path: Path) -> Dict[str, Any]:
    if not path.exists():
        raise FileNotFoundError(f"No existe: {path}")
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def safe_text(v: Any) -> str:
    if v is None:
        return ""
    return str(v).strip()


def build_pdf(manifest_path: str, charts_dir: str, output_pdf: str) -> None:
    manifest = load_json(Path(manifest_path))
    charts_base = Path(charts_dir)

    title = safe_text(manifest.get("title") or "Reporte ejecutivo")
    notebook_path = safe_text(manifest.get("notebook_path") or "N/D")
    insights = manifest.get("insights") or []
    conclusion = safe_text(manifest.get("conclusion") or "No se encontró una conclusión explícita en el notebook.")
    charts = manifest.get("charts") or []

    doc = SimpleDocTemplate(
        output_pdf,
        pagesize=A4,
        leftMargin=1.6 * cm,
        rightMargin=1.6 * cm,
        topMargin=1.4 * cm,
        bottomMargin=1.4 * cm,
    )

    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name="BodyES", fontSize=11, leading=15))
    styles.add(ParagraphStyle(name="SmallES", fontSize=9, leading=12))

    story = []
    story.append(Paragraph(title, styles["Title"]))
    story.append(Paragraph("Reporte generado automáticamente desde framework de extracción de notebooks", styles["Heading2"]))
    story.append(Spacer(1, 0.25 * cm))
    story.append(Paragraph(f"<b>Notebook origen:</b> {notebook_path}", styles["BodyES"]))
    story.append(Paragraph(f"<b>Insights detectados:</b> {len(insights)} | <b>Gráficos detectados:</b> {len(charts)}", styles["BodyES"]))
    story.append(Spacer(1, 0.35 * cm))

    if insights:
        story.append(Paragraph("Insights clave", styles["Heading2"]))
        for idx, ins in enumerate(insights[:10], 1):
            story.append(Paragraph(f"{idx}. {safe_text(ins)}", styles["BodyES"]))
            story.append(Spacer(1, 0.08 * cm))
        story.append(Spacer(1, 0.2 * cm))

    story.append(Paragraph("Conclusión", styles["Heading2"]))
    story.append(Paragraph(conclusion, styles["BodyES"]))
    story.append(Spacer(1, 0.35 * cm))

    if charts:
        story.append(Paragraph("Gráficos extraídos", styles["Heading2"]))
        story.append(Spacer(1, 0.15 * cm))

        for idx, chart in enumerate(charts, 1):
            chart_file = charts_base / chart["filename"]
            if not chart_file.exists():
                continue
            caption = safe_text(chart.get("caption") or f"Gráfico {idx}")
            story.append(Paragraph(f"<b>{caption}</b>", styles["BodyES"]))
            story.append(Spacer(1, 0.08 * cm))
            story.append(Image(str(chart_file), width=16.5 * cm, height=9.5 * cm))
            story.append(Spacer(1, 0.08 * cm))
            story.append(Paragraph(f"Fuente: celda {chart.get('source_cell_index', 'N/D')}", styles["SmallES"]))
            story.append(Spacer(1, 0.35 * cm))

    doc.build(story)


def main() -> None:
    if len(sys.argv) < 4:
        print("Uso: python generate_pdf_from_framework.py <manifest.json> <charts_dir> <output.pdf>")
        sys.exit(1)

    manifest_path = sys.argv[1]
    charts_dir = sys.argv[2]
    output_pdf = sys.argv[3]

    build_pdf(manifest_path, charts_dir, output_pdf)
    print(f"PDF generado: {output_pdf}")


if __name__ == "__main__":
    main()
