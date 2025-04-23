import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Cargar la hoja específica del archivo Excel
file_path = "data/Internet.xlsx"
data = pd.read_excel(file_path, sheet_name='Penetracion-hogares')

# Verificar y asegurar que la columna 'Provincia' es texto
if 'Provincia' in data.columns:
    data['Provincia'] = data['Provincia'].astype(str).str.strip()  # Convertir a texto y eliminar espacios
    data = data.dropna(subset=['Provincia'])  # Eliminar nulos en 'Provincia'

# **KPI propuesto: Incremento del 2% en accesos por cada 100 hogares**
if 'Accesos por cada 100 hogares' in data.columns:
    data['Nuevo Acceso'] = data['Accesos por cada 100 hogares'] * 1.02  # Simular un 2% de incremento
    data['KPI Incremento'] = ((data['Nuevo Acceso'] - data['Accesos por cada 100 hogares']) / 
                              data['Accesos por cada 100 hogares']) * 100

# Inicializar la columna 'Cumple Objetivo' como tipo texto para evitar el KeyError
data['Cumple Objetivo'] = np.nan  # Crear la columna y llenarla con valores NaN inicialmente

# Ordenar por provincia, año y trimestre para comparar períodos
data = data.sort_values(by=['Provincia', 'Año', 'Trimestre'], ascending=True)

# Procesar todas las provincias individualmente
for provincia in data['Provincia'].unique():
    province_data = data[data['Provincia'] == provincia]  # Filtrar datos por provincia
    for i in range(len(province_data)):
        # Evaluar únicamente si hay un trimestre anterior (ignorar el primero)
        if i > 0:
            prev_index = province_data.index[i - 1]
            current_index = province_data.index[i]
            # Comparar KPI calculado con el acceso real del trimestre actual
            if province_data.loc[current_index, 'Accesos por cada 100 hogares'] >= province_data.loc[prev_index, 'Nuevo Acceso']:
                data.loc[current_index, 'Cumple Objetivo'] = 'Alcanzado'
            elif province_data.loc[current_index, 'Accesos por cada 100 hogares'] >= province_data.loc[prev_index, 'Accesos por cada 100 hogares']:
                data.loc[current_index, 'Cumple Objetivo'] = 'Cerca de alcanzar'
            else:
                data.loc[current_index, 'Cumple Objetivo'] = 'No alcanzado'

# Filtro interactivo por provincia
provincia = st.sidebar.selectbox("Selecciona una provincia:", data['Provincia'].unique())
filtered_data = data[data['Provincia'] == provincia]  # Definir el DataFrame filtrado

# Redondear valores para los gráficos
rounded_values = np.round(filtered_data['Accesos por cada 100 hogares'], 2)

# Asegurar que todas las columnas numéricas tengan 2 decimales
pd.options.display.float_format = '{:.2f}'.format  # Formato de número global en pandas

# Redondear columnas numéricas en la tabla filtrada
filtered_data = filtered_data.round(2)

# Tabla de KPIs con colores según el cumplimiento del objetivo
def highlight_kpi(row):
    if row['Cumple Objetivo'] == 'Alcanzado':
        return ['background-color: green'] * len(row)
    elif row['Cumple Objetivo'] == 'Cerca de alcanzar':
        return ['background-color: yellow'] * len(row)
    elif row['Cumple Objetivo'] == 'No alcanzado':
        return ['background-color: red'] * len(row)
    else:
        return [''] * len(row)

st.subheader(f"Tabla de KPIs con colores según el cumplimiento del objetivo para la provincia seleccionada ({provincia})")
# Aplicar formato a la tabla para garantizar que las columnas numéricas se muestren con dos decimales
styled_data = filtered_data.style.format({
    'Accesos por cada 100 hogares': '{:.2f}',
    'Nuevo Acceso': '{:.2f}',
    'KPI Incremento': '{:.2f}'
}).apply(highlight_kpi, axis=1)  # Aplicar estilo por fila
st.dataframe(styled_data)

# Graficar el indicador de 'Accesos por cada 100 hogares' por trimestre y año
if 'Accesos por cada 100 hogares' in filtered_data.columns:
    plt.figure(figsize=(10, 5))
    plt.bar(
        filtered_data['Trimestre'].astype(str) + " " + filtered_data['Año'].astype(str),
        rounded_values,
        color='skyblue'
    )
    plt.title(f"Accesos por cada 100 hogares - {provincia}")
    plt.xlabel("Trimestre y Año")
    plt.ylabel("Accesos por cada 100 hogares")
    plt.xticks(rotation=90)
    plt.grid(axis='y', linestyle='--', alpha=0.7)  # Agrega líneas horizontales al eje Y
    st.pyplot(plt)

# Gráfico del promedio de accesos por provincia (sin filtro)
if 'Accesos por cada 100 hogares' in data.columns:
    st.subheader("Promedio de accesos por cada 100 hogares por provincia")
    avg_accesos = data.groupby('Provincia')['Accesos por cada 100 hogares'].mean()
    plt.figure(figsize=(10, 5))
    avg_accesos.plot(kind='bar', color='green')
    plt.title("Promedio de Accesos por cada 100 hogares por Provincia")
    plt.ylabel("Accesos por cada 100 hogares")
    plt.xticks(rotation=90)
    plt.grid(axis='y', linestyle='--', alpha=0.7)  # Agrega líneas horizontales al eje Y
    st.pyplot(plt)

# Mostrar la estructura inicial de los datos
st.title("Acceso por cada 100 hogares")
st.sidebar.title("Filtros")
st.subheader("Vista previa de los datos")
st.write(data)