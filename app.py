import pandas as pd
import plotly.express as px
import streamlit as st


st.set_page_config(page_title='Anuncios de venta de coches', layout='wide')


@st.cache_data
def load_data():
    return pd.read_csv('vehicles_us.csv')


df = load_data()
st.header('Análisis de anuncios de venta de coches en EE.UU.')
st.write(
    f'Conjunto de datos con {len(df):,} anuncios. '
    'Marca las casillas para construir los gráficos.'
)

if st.checkbox('Mostrar los datos'):
    st.dataframe(df.head(100))


if st.checkbox('Construir un histograma'):
    st.write('Distribución del kilometraje (odómetro) de los vehículos')
    fig = px.histogram(df, x='odometer', nbins=50,
                       title='Distribución del odómetro')
    fig.update_layout(
        xaxis_title='Kilometraje (millas)',
        yaxis_title='Cantidad de anuncios de coche',
        title_font=dict(size=32, weight='bold')
    )
    st.plotly_chart(fig, use_container_width=True)

if st.checkbox('Construir un gráfico de dispersión'):
    st.write('Relación entre el kilometraje y el precio')
    fig = px.scatter(df, x='odometer', y='price', color='condition',
                     opacity=0.5, title='Relacion entre kilometraje y precio del coche')
    fig.update_layout(
        xaxis_title='Kilometraje (millas)',
        yaxis_title='Precio (USD)',
        title_font=dict(size=32, weight='bold')
    )
    st.plotly_chart(fig, use_container_width=True)
