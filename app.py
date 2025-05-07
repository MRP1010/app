import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Proyecto 7 Aplicación Web')

data_cars = pd.read_csv('vehicles_us.csv')               

crea_hist = st.button('Generar Histograma') 

if crea_hist:
   
   fig = px.histogram(data_cars, x="odometer")

   st.plotly_chart(fig, use_container_width=True)

crea_dist = st.button('Genera gráfico de dispersión')  

if crea_dist:  

    fig = px.scatter(data_cars, x="odometer", y="price")

    st.plotly_chart(fig, use_container_width=True)