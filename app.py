import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles.csv')



build_dispersao = st.checkbox('Criar um grafico de dispersão')
if build_dispersao:
            st.write('Criando um grafico de dispersão, por favor aguarde...')
            fig1 = px.scatter(car_data, x="odometer", y="price") # criar um gráfico de dispersão
            st.plotly_chart(fig1, use_container_width=True)


hist_button = st.button('Criar histograma')
        
if hist_button:
            st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
            fig = px.histogram(car_data, x="odometer")
            st.plotly_chart(fig, use_container_width=True)


