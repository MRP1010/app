import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Proyecto 7 Aplicación Web')

data_cars = pd.read_csv('vehicles_us.csv')   # leer los datos           

crea_hist = st.button('Generar Histograma')  # crear un botón

if crea_hist: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    # crear un histograma
    fig = px.histogram(data_cars, x="odometer")
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

crea_dist = st.button('Generar gráfico de dispersión')  # crea el segundo  botón

if crea_dist:# al hacer clic en el botón
    # escribir un mensaje
    st.write('Gráfico de dispersión')
    # crear la distribución
    fig = px.scatter(data_cars, x="odometer", y="price")
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

crea_hist = st.checkbox('Seleccione para generar el histograma')  # crear un botón

if crea_hist: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    # crear un histograma
    fig = px.histogram(data_cars, x="odometer")
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

crea_dist = st.checkbox('Seleccione para construir gráfico de dispersión')  # crea el segundo  botón

if crea_dist:# al hacer clic en el botón
    # escribir un mensaje
    st.write('Gráfico de dispersión')
    # crear la distribución
    fig = px.scatter(data_cars, x="odometer", y="price")
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
