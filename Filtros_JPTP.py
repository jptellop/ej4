import streamlit as st
import pandas as pd

# 1. Cargar datos
df = pd.read_csv("cars.csv")

# 2. Crear filtro en barra lateral
opcion = st.sidebar.selectbox('Filtra por categoría', df['categoria'].unique())

# 3. Aplicar filtro
df_filtrado = df[df['categoria'] == opcion]

# 4. Mostrar resultado
st.write("Datos filtrados:", df_filtrado)
