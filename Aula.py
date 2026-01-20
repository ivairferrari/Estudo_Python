# Importar as bibliotecas
import streamlit as st
import pandas as pd
import yfinance as yf

# Criar as funções de carregamento de dados
@st.cache_data
def carregar_dados(empresa):
    dados_acao = yf.Ticker(empresa)
    cotacoes_acao = dados_acao.history(start="2010-01-01", end="2025-12-31")
    cotacoes_acao =  cotacoes_acao[["Close"]]
    return cotacoes_acao
    
# --- CRIAR A INTERFACE DO STREAMLIT ---

st.write("# App Preço de Ações")

# Criar uma caixa de texto para o usuário digitar o ticker
# O 'value' é o valor padrão que já vem preenchido
ticker = st.text_input("Digite o Ticker da empresa (ex: ITUB4.SA, PETR4.SA, AAPL):", value="ITUB4.SA")

# Chamamos a função passando o que o usuário digitou
dados = carregar_dados(ticker)

st.write(f"""
O Gráfico abaixo mostra a evolução do preço das ações da **{ticker}** de 2010 a 2024.
         """)

# Criar o gráfico
# Se o ticker for inválido, o yfinance retorna vazio, então verificamos se há dados
if not dados.empty:
    st.line_chart(dados)
else:
    st.error("Não foi possível encontrar dados para este Ticker. Verifique se escreveu corretamente (ex: PETR4.SA).")

st.write("# Fim do APP")