# App Streamlit: Titanic Dashboard

## Archivos
- `app_titanic_streamlit.py`
- `requirements_streamlit_app.txt`

## Dónde ponerlos
Mueve ambos a la raíz de tu proyecto `analisis-datos-ia/`.

## Ejecutar localmente
```bash
cd ~/analisis-datos-ia
source .venv/bin/activate
python3 -m pip install -r requirements_streamlit_app.txt
streamlit run app_titanic_streamlit.py
```

## Importante
La app espera encontrar el dataset en:
`data/raw/titanic.csv`

## Qué muestra
- filtros por sexo, clase, puerto y edad
- KPIs principales
- gráficos de supervivencia
- hallazgos ejecutivos
- tabla filtrable
