from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


def run_cmd(cmd: list[str], cwd: Path | None = None) -> None:
    print(f"\n>>> Ejecutando: {' '.join(cmd)}")
    result = subprocess.run(cmd, cwd=str(cwd) if cwd else None)
    if result.returncode != 0:
        raise SystemExit(result.returncode)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Pipeline completo: extraer notebook -> generar PDF -> generar PPTX"
    )
    parser.add_argument(
        "notebook",
        help="Ruta al notebook .ipynb que quieres procesar"
    )
    parser.add_argument(
        "--output-dir",
        default="outputs/extraccion_auto",
        help="Carpeta donde se guardará la extracción del framework"
    )
    parser.add_argument(
        "--pdf-output",
        default="outputs/reporte_ejecutivo.pdf",
        help="Ruta del PDF final"
    )
    parser.add_argument(
        "--pptx-output",
        default="outputs/reporte_ejecutivo.pptx",
        help="Ruta del PPTX final"
    )
    parser.add_argument(
        "--python-bin",
        default=sys.executable,
        help="Ruta del binario de Python a usar"
    )
    args = parser.parse_args()

    project_root = Path.cwd()
    notebook_path = project_root / args.notebook
    output_dir = project_root / args.output_dir
    charts_dir = output_dir / "charts"
    manifest_path = output_dir / "report_manifest.json"
    pdf_output = project_root / args.pdf_output
    pptx_output = project_root / args.pptx_output

    framework_script = project_root / "notebook_report_framework.py"
    pdf_script = project_root / "generate_pdf_from_framework.py"
    pptx_script = project_root / "generate_pptx_from_framework.py"

    required_files = [
        notebook_path,
        framework_script,
        pdf_script,
        pptx_script,
    ]

    missing = [str(p) for p in required_files if not p.exists()]
    if missing:
        print("Faltan archivos requeridos:")
        for m in missing:
            print(f" - {m}")
        raise SystemExit(1)

    pdf_output.parent.mkdir(parents=True, exist_ok=True)
    pptx_output.parent.mkdir(parents=True, exist_ok=True)

    # Paso 1: extracción del notebook
    run_cmd([
        args.python_bin,
        str(framework_script),
        str(notebook_path),
        "--output-dir",
        str(output_dir)
    ])

    # Validación extracción
    if not manifest_path.exists():
        print(f"No se generó el manifest esperado: {manifest_path}")
        raise SystemExit(1)

    if not charts_dir.exists():
        print(f"No se generó la carpeta de gráficos esperada: {charts_dir}")
        raise SystemExit(1)

    # Paso 2: PDF
    run_cmd([
        args.python_bin,
        str(pdf_script),
        str(manifest_path),
        str(charts_dir),
        str(pdf_output)
    ])

    # Paso 3: PPTX
    run_cmd([
        args.python_bin,
        str(pptx_script),
        str(manifest_path),
        str(charts_dir),
        str(pptx_output)
    ])

    print("\nPipeline completado correctamente.")
    print(f"Manifest: {manifest_path}")
    print(f"Charts:   {charts_dir}")
    print(f"PDF:      {pdf_output}")
    print(f"PPTX:     {pptx_output}")


if __name__ == "__main__":
    main()
