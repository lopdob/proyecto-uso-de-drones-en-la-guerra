import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Uso de Drones en la Guerra",
    page_icon="🚁",
    layout="wide"
)

st.title("🚁 Aplicativo Web: Uso de Drones en la Guerra")

st.markdown("""
### Descripción
Este aplicativo permite analizar drones militares empleados en conflictos modernos,
comparar características y conocer sus principales funciones.
""")

# Base de datos
datos = {
    "Drone": [
        "MQ-9 Reaper",
        "Bayraktar TB2",
        "RQ-4 Global Hawk",
        "Switchblade 600",
        "Orlan-10"
    ],
    "País": [
        "Estados Unidos",
        "Turquía",
        "Estados Unidos",
        "Estados Unidos",
        "Rusia"
    ],
    "Función": [
        "Ataque y vigilancia",
        "Reconocimiento y ataque",
        "Reconocimiento estratégico",
        "Munición merodeadora",
        "Reconocimiento"
    ],
    "Alcance (km)": [
        1850,
        300,
        22000,
        80,
        120
    ]
}

df = pd.DataFrame(datos)

st.subheader("Base de Datos de Drones")
st.dataframe(df, use_container_width=True)

st.subheader("Buscar Drone")

drone = st.selectbox(
    "Seleccione un drone",
    df["Drone"]
)

info = df[df["Drone"] == drone]

st.write(info)

st.subheader("Recomendación según misión")

mision = st.selectbox(
    "Tipo de misión",
    [
        "Reconocimiento",
        "Vigilancia",
        "Ataque"
    ]
)

if st.button("Analizar"):

    if mision == "Reconocimiento":
        st.success("Drone recomendado: RQ-4 Global Hawk")
        st.write("Alta autonomía y capacidad de vigilancia estratégica.")

    elif mision == "Vigilancia":
        st.success("Drone recomendado: Bayraktar TB2")
        st.write("Adecuado para observación continua del campo de batalla.")

    else:
        st.success("Drone recomendado: MQ-9 Reaper")
        st.write("Capaz de realizar ataques de precisión y vigilancia.")

st.subheader("Distribución de Funciones")

funciones = {
    "Reconocimiento": 40,
    "Vigilancia": 35,
    "Ataque": 25
}

st.bar_chart(funciones)

st.markdown("---")
st.caption("Proyecto académico sobre el empleo de drones en conflictos armados.")
