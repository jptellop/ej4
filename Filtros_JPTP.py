import streamlit as st
import pandas as pd

# 1. Cargar datos
df = pd.read_csv("cars.csv")

# 2. Crear filtro en barra lateral
opcion = st.sidebar.selectbox('Filtrar por categoría', df['mpg'].unique())

# 3. Aplicar filtro
df_filtrado = df[df['mpg'] == opcion]

# 4. Mostrar resultado
st.write("Datos filtrados:", df_filtrado)
