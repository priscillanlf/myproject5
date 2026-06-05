import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv("vehicles.csv")

st.header("Dashboard de Análise de Veículos")

hist_button = st.button("Criar histograma")

if hist_button:
    st.write("Criando histograma do odômetro...")

    fig = px.histogram(car_data, x="odometer")

    st.plotly_chart(fig, use_container_width=True)
    
scatter_button = st.button("Criar gráfico de dispersão")

if scatter_button:
    st.write("Criando gráfico de dispersão...")

    fig = px.scatter(car_data, x="odometer", y="price")

    st.plotly_chart(fig, use_container_width=True)
    
    

