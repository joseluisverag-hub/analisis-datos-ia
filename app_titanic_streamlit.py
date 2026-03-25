import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(page_title="Titanic Dashboard", layout="wide")

@st.cache_data
def load_data():
    df = pd.read_csv("data/raw/titanic.csv")
    df["Age"] = df["Age"].fillna(df["Age"].median())
    df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
    df = df.drop(columns=["Cabin"])
    df["grupo_edad"] = pd.cut(
        df["Age"],
        bins=[0, 12, 18, 60, 100],
        labels=["Niño", "Adolescente", "Adulto", "Adulto Mayor"]
    )
    df["tamano_familia"] = df["SibSp"] + df["Parch"] + 1
    return df

df = load_data()

st.title("Titanic: análisis de datos + IA aplicada")
st.markdown(
    """
    Dashboard ejecutivo basado en el análisis exploratorio del Titanic.
    Incluye filtros, KPIs, visualizaciones e insights clave.
    """
)

with st.sidebar:
    st.header("Filtros")
    sex_options = st.multiselect("Sexo", options=sorted(df["Sex"].dropna().unique()), default=sorted(df["Sex"].dropna().unique()))
    class_options = st.multiselect("Clase", options=sorted(df["Pclass"].dropna().unique()), default=sorted(df["Pclass"].dropna().unique()))
    embark_options = st.multiselect("Puerto de embarque", options=sorted(df["Embarked"].dropna().unique()), default=sorted(df["Embarked"].dropna().unique()))
    age_range = st.slider("Rango de edad", int(df["Age"].min()), int(df["Age"].max()), (int(df["Age"].min()), int(df["Age"].max())))

filtered = df[
    (df["Sex"].isin(sex_options)) &
    (df["Pclass"].isin(class_options)) &
    (df["Embarked"].isin(embark_options)) &
    (df["Age"].between(age_range[0], age_range[1]))
].copy()

total = len(filtered)
survival_rate = filtered["Survived"].mean() if total else 0
avg_age = filtered["Age"].mean() if total else 0
avg_fare = filtered["Fare"].mean() if total else 0

c1, c2, c3, c4 = st.columns(4)
c1.metric("Pasajeros filtrados", f"{total}")
c2.metric("Tasa de supervivencia", f"{survival_rate:.1%}")
c3.metric("Edad promedio", f"{avg_age:.1f}")
c4.metric("Tarifa promedio", f"{avg_fare:.2f}")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Supervivencia por sexo")
    fig, ax = plt.subplots(figsize=(6, 4))
    filtered.groupby("Sex")["Survived"].mean().plot(kind="bar", ax=ax)
    ax.set_ylim(0, 1)
    ax.set_ylabel("Proporción")
    ax.set_xlabel("Sexo")
    st.pyplot(fig)

with col2:
    st.subheader("Supervivencia por clase")
    fig, ax = plt.subplots(figsize=(6, 4))
    filtered.groupby("Pclass")["Survived"].mean().plot(kind="bar", ax=ax)
    ax.set_ylim(0, 1)
    ax.set_ylabel("Proporción")
    ax.set_xlabel("Clase")
    st.pyplot(fig)

col3, col4 = st.columns(2)

with col3:
    st.subheader("Supervivencia por grupo etario")
    fig, ax = plt.subplots(figsize=(6, 4))
    filtered.groupby("grupo_edad", observed=False)["Survived"].mean().plot(kind="bar", ax=ax)
    ax.set_ylim(0, 1)
    ax.set_ylabel("Proporción")
    ax.set_xlabel("Grupo etario")
    st.pyplot(fig)

with col4:
    st.subheader("Supervivencia por tamaño de familia")
    fig, ax = plt.subplots(figsize=(6, 4))
    filtered.groupby("tamano_familia")["Survived"].mean().plot(kind="bar", ax=ax)
    ax.set_ylim(0, 1)
    ax.set_ylabel("Proporción")
    ax.set_xlabel("Tamaño de familia")
    st.pyplot(fig)

st.subheader("Hallazgos ejecutivos")
st.markdown(
    """
- El sexo aparece como uno de los factores más influyentes: las mujeres muestran mejor supervivencia que los hombres.
- La clase del pasajero también tiene una relación fuerte con la supervivencia, con ventaja para primera clase.
- Niños y grupos familiares pequeños o medianos tienden a mostrar mejores resultados que adultos mayores, pasajeros solos o familias muy grandes.
- Este dashboard permite explorar esos patrones con filtros simples para una audiencia no técnica.
"""
)

st.subheader("Vista de datos")
st.dataframe(
    filtered[["PassengerId", "Survived", "Pclass", "Name", "Sex", "Age", "Fare", "Embarked", "grupo_edad", "tamano_familia"]]
    .reset_index(drop=True),
    use_container_width=True
)

st.caption("App creada con Streamlit a partir del análisis del Titanic en Python.")
