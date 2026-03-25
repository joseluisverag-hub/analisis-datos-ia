# Automatización de reporte ejecutivo desde notebook

## Idea
En vez de copiar métricas manualmente, el notebook exporta un archivo JSON con:
- métricas
- resumen ejecutivo
- hallazgos clave
- recomendaciones

Luego un script Python consume ese JSON y genera:
- PowerPoint (`.pptx`)
- PDF (`.pdf`)
- gráficos PNG

## Archivos
- `generar_reporte_desde_notebook.py`: generador principal
- `celda_payload_para_notebook.py`: celda ejemplo para pegar al final del notebook

## Flujo recomendado

### 1) En tu notebook
Agrega una celda final que escriba:
`../outputs/report_payload_titanic.json`

### 2) Instala dependencias
```bash
pip install matplotlib python-pptx reportlab
```

### 3) Ejecuta el notebook
Debe generarse:
`outputs/report_payload_titanic.json`

### 4) Genera el PPTX y PDF
```bash
python generar_reporte_desde_notebook.py   --payload outputs/report_payload_titanic.json   --outdir outputs/reportes   --basename reporte_titanic_ejecutivo
```

## Salidas esperadas
En `outputs/reportes/`:
- `reporte_titanic_ejecutivo.pptx`
- `reporte_titanic_ejecutivo.pdf`
- gráficos PNG

## Por qué este enfoque
Es más estable que intentar "leer" texto libre del notebook.
El notebook sigue siendo tu fuente de verdad, pero exporta un payload estructurado reutilizable.

## Siguiente mejora posible
Automatizar el cálculo del payload para que las métricas salgan directo de `df_model`
en la misma celda final, sin hardcodear valores.