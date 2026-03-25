# Análisis de Datos + IA Aplicada

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-purple)
![DuckDB](https://img.shields.io/badge/DuckDB-SQL%20Analytics-yellow)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![PDF](https://img.shields.io/badge/Output-PDF-success)
![PowerPoint](https://img.shields.io/badge/Output-PPTX-informational)

Proyecto de portafolio enfocado en **análisis de datos con Python**, **SQL**, **visualización ejecutiva**, **IA aplicada** y **automatización de reportes gerenciales** en **PDF** y **PowerPoint**.

---

## Tabla de contenidos

- [Propuesta de valor](#propuesta-de-valor)
- [Objetivo del proyecto](#objetivo-del-proyecto)
- [Stack tecnológico](#stack-tecnológico)
- [Estructura del proyecto](#estructura-del-proyecto)
- [Caso aplicado: Titanic](#caso-aplicado-titanic)
- [Pipeline de automatización](#pipeline-de-automatización)
- [Convención para que el framework funcione bien](#convención-para-que-el-framework-funcione-bien)
- [Instalación](#instalación)
- [Cómo ejecutar el proyecto](#cómo-ejecutar-el-proyecto)
- [Generación automática de PDF y PPTX](#generación-automática-de-pdf-y-pptx)
- [Salidas generadas](#salidas-generadas)
- [Ejecución paso a paso manual](#ejecución-paso-a-paso-manual)
- [Qué demuestra este proyecto](#qué-demuestra-este-proyecto)
- [Valor para negocio](#valor-para-negocio)
- [Próximos pasos](#próximos-pasos)
- [Autor](#autor)

---

## Propuesta de valor

Este proyecto no solo demuestra capacidad para analizar datos, sino también para **transformar resultados técnicos en entregables ejecutivos reutilizables**.

El flujo completo permite:

- explorar y limpiar datos
- analizar con pandas y SQL
- generar visualizaciones
- redactar insights y conclusiones
- extraer automáticamente contenido clave desde notebooks
- producir reportes ejecutivos en **PDF** y **PPTX**
- ejecutar todo con **un solo comando**

---

## Objetivo del proyecto

Construir un pipeline reproducible que demuestre capacidades de:

- análisis exploratorio de datos
- transformación y limpieza de información
- consultas SQL para responder preguntas de negocio
- storytelling con visualizaciones
- uso de IA aplicada para convertir hallazgos técnicos en lenguaje ejecutivo
- automatización de reportes ejecutivos

---

## Stack tecnológico

- **Python**
- **pandas**
- **matplotlib**
- **DuckDB**
- **Jupyter Notebook**
- **Git / GitHub**
- **Streamlit**
- **python-pptx**
- **reportlab**

---

## Estructura del proyecto

```text
analisis-datos-ia/
├─ data/
├─ notebooks/
├─ outputs/
├─ src/
├─ app_titanic_streamlit.py
├─ notebook_report_framework.py
├─ generate_pdf_from_framework.py
├─ generate_pptx_from_framework.py
├─ run_pipeline.py
├─ queries.sql
├─ requirements.txt
├─ README.md
└─ .gitignore
```

### Archivos principales

- `notebook_report_framework.py`  
  Framework reutilizable que extrae automáticamente desde un notebook:
  - título
  - insights
  - conclusión
  - gráficos embebidos en outputs

- `generate_pdf_from_framework.py`  
  Genera un **PDF ejecutivo** a partir de:
  - `report_manifest.json`
  - carpeta `charts/`

- `generate_pptx_from_framework.py`  
  Genera una **presentación ejecutiva en PowerPoint** a partir de:
  - `report_manifest.json`
  - carpeta `charts/`

- `run_pipeline.py`  
  Ejecuta todo el flujo con **un solo comando**:
  1. extracción del notebook
  2. generación del PDF
  3. generación del PPTX

- `app_titanic_streamlit.py`  
  App interactiva del caso Titanic.

---

## Caso aplicado: Titanic

El proyecto utiliza el dataset **Titanic** para demostrar un flujo completo de trabajo en analítica:

- exploración inicial
- tratamiento de nulos
- análisis con pandas
- consultas SQL con DuckDB
- visualización ejecutiva
- insights escritos en markdown
- conclusión ejecutiva
- automatización de reportes

---

## Pipeline de automatización

El flujo final del proyecto es:

```text
notebook.ipynb
   -> notebook_report_framework.py
   -> report_manifest.json + charts/
   -> generate_pdf_from_framework.py
   -> generate_pptx_from_framework.py
   -> run_pipeline.py
```

### Flujo explicado

1. Se desarrolla el análisis en un notebook.
2. El framework extrae automáticamente:
   - título
   - insights
   - conclusión
   - gráficos
3. Se genera un `report_manifest.json` y una carpeta `charts/`.
4. A partir de esos archivos se construyen:
   - un **PDF ejecutivo**
   - un **PPTX ejecutivo**
5. Todo el proceso puede correrse con un solo comando.

---

## Convención para que el framework funcione bien

Para que el extractor automático funcione correctamente, el notebook debe seguir una convención mínima:

### Título
Primera celda markdown con:

```markdown
# Título del análisis
```

### Insights
Después de cada gráfico o bloque analítico importante, debe existir una celda markdown como:

```markdown
## Insight
Texto del insight.
```

### Conclusión
Al final del notebook debe existir una celda markdown como:

```markdown
## Conclusión
Texto de cierre ejecutivo.
```

### Gráficos
Los gráficos deben estar visibles como **output** del notebook.

---

## Instalación

### 1. Clonar el proyecto
```bash
git clone <tu-repo>
cd analisis-datos-ia
```

### 2. Crear y activar entorno virtual
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Instalar dependencias adicionales para reportes
Si no están en `requirements.txt`, instala:

```bash
pip install python-pptx reportlab
```

---

## Cómo ejecutar el proyecto

### A. Ejecutar notebooks
Abre los notebooks en VS Code o Jupyter y ejecuta el flujo del análisis.

Ejemplo de notebook principal:

```text
notebooks/04_visualizacion_storytelling.ipynb
```

---

## Generación automática de PDF y PPTX

### Opción recomendada: un solo comando

Desde la raíz del proyecto:

```bash
python3 run_pipeline.py notebooks/04_visualizacion_storytelling.ipynb \
  --output-dir outputs/extraccion_titanic \
  --pdf-output outputs/reporte_ejecutivo.pdf \
  --pptx-output outputs/reporte_ejecutivo.pptx
```

### Qué hace ese comando

Ese comando ejecuta automáticamente:

1. **Extracción del notebook**
   - crea `report_manifest.json`
   - extrae gráficos a `charts/`

2. **Generación del PDF**
   - crea `outputs/reporte_ejecutivo.pdf`

3. **Generación del PowerPoint**
   - crea `outputs/reporte_ejecutivo.pptx`

---

## Salidas generadas

Después de correr el pipeline, deberías obtener algo como esto:

```text
outputs/
├─ extraccion_titanic/
│  ├─ report_manifest.json
│  ├─ report_extracted.md
│  └─ charts/
│     ├─ chart_01.png
│     ├─ chart_02.png
│     └─ ...
├─ reporte_ejecutivo.pdf
└─ reporte_ejecutivo.pptx
```

---

## Ejecución paso a paso manual

Si no quieres usar `run_pipeline.py`, puedes correr cada parte por separado.

### 1. Extraer contenido del notebook
```bash
python3 notebook_report_framework.py notebooks/04_visualizacion_storytelling.ipynb --output-dir outputs/extraccion_titanic
```

### 2. Generar PDF
```bash
python3 generate_pdf_from_framework.py outputs/extraccion_titanic/report_manifest.json outputs/extraccion_titanic/charts outputs/reporte_ejecutivo.pdf
```

### 3. Generar PPTX
```bash
python3 generate_pptx_from_framework.py outputs/extraccion_titanic/report_manifest.json outputs/extraccion_titanic/charts outputs/reporte_ejecutivo.pptx
```

---

## Qué demuestra este proyecto

Este proyecto demuestra capacidades útiles para roles como:

- **Data Analyst**
- **BI Analyst**
- **Analytics Translator**
- **Reporting Analyst**
- **Business Insights Analyst**
- **Data + IA aplicada**

### Competencias evidenciadas

- análisis con Python
- SQL para preguntas de negocio
- visualización de datos
- comunicación ejecutiva
- IA aplicada a síntesis de hallazgos
- automatización de entregables
- diseño de pipelines reproducibles

---

## Valor para negocio

El valor del proyecto no está solo en analizar datos, sino en **convertir análisis en decisiones**.

Este pipeline permite que un análisis en notebook termine convertido en:

- un **PDF formal**
- una **presentación ejecutiva**
- una **base reutilizable** para otros datasets o reportes

Esto reduce tiempo manual de reporting y mejora la consistencia de entregables.

---

## Próximos pasos

- integrar más notebooks al pipeline
- extender el framework para extraer también tablas clave
- enriquecer la app Streamlit
- incorporar modelos predictivos
- automatizar publicación de reportes por lote

---

## Estándar de notebooks para reutilización

Este proyecto también define un estándar para estructurar notebooks de forma compatible con el framework de extracción automática.

Ese estándar está documentado en un archivo separado para reutilizarlo en próximos proyectos y para aplicarlo con GitHub Copilot en VS Code.

Archivo recomendado:
- `PROMPT_ESTANDAR_NOTEBOOK_COPILOT.md`

---

## Autor

**José Vera**

Proyecto de portafolio orientado a demostrar capacidades de **Análisis de Datos + IA aplicada**, con foco en transformar resultados analíticos en entregables ejecutivos automatizados.
