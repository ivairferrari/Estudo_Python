# Importar as bibliotecas
import streamlit as st
import pandas as pd
import yfinance as yf

# Criar as funções de carregamento de dados
@st.cache_data
def carregar_dados(empresa):
    texto_tickers = " ".join(empresa)
    dados_acao = yf.Tickers(texto_tickers)
    cotacoes_acao = dados_acao.history(start="2010-01-01", end="2024-12-31")
    
    cotacoes_acao =  cotacoes_acao["Close"]
    return cotacoes_acao

acoes=["ITUB4.SA", "PETR4.SA", "VALE3.SA", "ABEV3.SA"]
dados = carregar_dados(acoes)

# criar a interface do streamlit
st.write("""
# App Preço de Ações
O Gráfico abaixo mostra a evolução do preço das ações ao longo dos anos.
         """)

# Prepara as visualizações - filtros
lista_acoes = st.multiselect("Escolhas as açõe para visualizar", dados.columns)
if lista_acoes:
        dados = dados[lista_acoes]
        if len(lista_acoes) == 1:
            acao_unica = lista_acoes[0]
            dados = dados.rename(columns={acao_unica: "Close"})      

# criar o gráfico
st.line_chart(dados)