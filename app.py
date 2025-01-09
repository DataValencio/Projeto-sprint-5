import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles.csv')


hist_button = st.button('Criar histograma')
        
if hist_button:
            st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
            fig = px.histogram(car_data, x="odometer")
            st.plotly_chart(fig, use_container_width=True)

disp_button = st.button('Criar um grafico de dispersão')

if disp_button:
            st.write('Criando um grafico de dispersão, por favor aguarde...')
            fig1 = px.scatter(car_data, x="odometer", y="price") # criar um gráfico de dispersão
            fig1.show()
            
