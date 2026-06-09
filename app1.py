import streamlit as st
import folium
from streamlit_folium import st_folium
from geopy.distance import geodesic

st.set_page_config(page_title="Simulador de Alcance de Drones", layout="wide")

st.title("🚁 Simulador de Alcance y Tiempo de Vuelo")

# Lista de drones
drones = {
    "DJI Mavic 3": 75,
    "Bayraktar TB2": 130,
    "MQ-9 Reaper": 480,
    "Switchblade 600": 185
}

# Configuración lateral
st.sidebar.header("Configuración")

radio_km = st.sidebar.slider(
    "Radio de alcance (km)",
    min_value=1,
    max_value=100,
    value=20
)

drone_seleccionado = st.sidebar.selectbox(
    "Drone principal",
    list(drones.keys())
)

velocidad = drones[drone_seleccionado]

st.write(f"Velocidad del drone seleccionado: **{velocidad} km/h**")

# Coordenadas iniciales (Lima)
lat_ini = -12.0464
lon_ini = -77.0428

# Crear mapa
m = folium.Map(
    location=[lat_ini, lon_ini],
    zoom_start=10
)

# Instrucciones
st.info("Haz clic en el mapa para colocar el punto de lanzamiento.")

# Mostrar mapa y capturar clics
map_data = st_folium(
    m,
    width=1000,
    height=600
)

if map_data["last_clicked"]:

    origen = (
        map_data["last_clicked"]["lat"],
        map_data["last_clicked"]["lng"]
    )

    # Nuevo mapa con punto y círculo
    m2 = folium.Map(
        location=origen,
        zoom_start=10
    )

    folium.Marker(
        origen,
        tooltip="Punto de lanzamiento"
    ).add_to(m2)

    folium.Circle(
        location=origen,
        radius=radio_km * 1000,
        color="blue",
        fill=True,
        fill_opacity=0.2
    ).add_to(m2)

    st.subheader("Punto de lanzamiento seleccionado")

    map_data2 = st_folium(
        m2,
        width=1000,
        height=600,
        key="mapa2"
    )

    if map_data2["last_clicked"]:

        destino = (
            map_data2["last_clicked"]["lat"],
            map_data2["last_clicked"]["lng"]
        )

        distancia = geodesic(origen, destino).km

        st.subheader("Resultados")

        st.write(f"📍 Distancia: **{distancia:.2f} km**")

        dentro = distancia <= radio_km

        if dentro:
            st.success("Objetivo dentro del radio de alcance.")
        else:
            st.error("Objetivo fuera del radio de alcance.")

        tabla = []

        for nombre, vel in drones.items():

            tiempo_horas = distancia / vel

            tabla.append({
                "Drone": nombre,
                "Velocidad (km/h)": vel,
                "Tiempo (min)": round(tiempo_horas * 60, 2)
            })

        st.dataframe(tabla, use_container_width=True)

        folium.Marker(
            destino,
            tooltip="Objetivo",
            icon=folium.Icon(color="red")
        ).add_to(m2)
