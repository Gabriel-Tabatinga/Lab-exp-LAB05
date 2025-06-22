import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Dashboard: Resultados do Experimento GraphQL vs REST")

# Carregar dados
df = pd.read_csv("resultados_experimento.csv")

st.header("Tabela de Dados Coletados")
st.dataframe(df)

# Estatísticas agrupadas
st.header("Resumo Estatístico")
resumo = df.groupby(['api', 'consulta_tipo']).agg(
    media_tempo_ms=('tempo_ms', 'mean'),
    desvio_tempo_ms=('tempo_ms', 'std'),
    media_tamanho_bytes=('tamanho_bytes', 'mean'),
    desvio_tamanho_bytes=('tamanho_bytes', 'std')
).reset_index()
st.dataframe(resumo)

# Gráficos
st.header("Tempo de Resposta (ms)")
fig1, ax1 = plt.subplots()
for api in df['api'].unique():
    for tipo in df['consulta_tipo'].unique():
        subset = df[(df['api'] == api) & (df['consulta_tipo'] == tipo)]
        ax1.plot(subset['tempo_ms'].values, label=f"{api} - {tipo}")
ax1.set_ylabel("Tempo (ms)")
ax1.set_xlabel("Execução")
ax1.legend()
st.pyplot(fig1)

st.header("Tamanho da Resposta (bytes)")
fig2, ax2 = plt.subplots()
for api in df['api'].unique():
    for tipo in df['consulta_tipo'].unique():
        subset = df[(df['api'] == api) & (df['consulta_tipo'] == tipo)]
        ax2.plot(subset['tamanho_bytes'].values, label=f"{api} - {tipo}")
ax2.set_ylabel("Tamanho (bytes)")
ax2.set_xlabel("Execução")
ax2.legend()
st.pyplot(fig2)

st.write("Dashboard gerado automaticamente. Analise os gráficos e tabelas para comparar o desempenho das APIs REST e GraphQL.")