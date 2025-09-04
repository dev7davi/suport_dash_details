import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Configurações da página
st.set_page_config(layout="wide", page_title="Dashboard de Chamados")
st.title("📊 Dashboard de Chamados por Área")

# Upload do arquivo Excel
uploaded_file = st.file_uploader("📂 Faça upload do arquivo Excel (.xlsx)", type="xlsx")

if uploaded_file:
    df = pd.read_excel(uploaded_file)

    # Agrupar e contar os registros por área
    area_counts = df['definicao_area'].value_counts().sort_values(ascending=True)

    # Cores personalizadas
    cores_personalizadas = {
        'GERAL': '#B0B0B0', 'PROPOSTA': '#F4A6AE', 'CLIENTES': '#CCCCCC',
        'DASHBOARD': '#FFE92E', 'RELATORIOS': '#AAAAAA', 'TABELA DE CONVENIO': '#E4362E',
        'EXTRATOS': '#BFBFBF', 'USUARIOS': '#B3B3B3', 'FINANCEIRO GERAL': '#00C000',
        'ATENDIMENTO': '#2E8BFF', 'CHAT': '#C85CF5', 'CAMPANHA': '#FFAE00',
        'AGENDAMENTO': '#999999', 'PESQUISADOR': '#FF00FF', 'STATUS DE PROPOSTA': '#D8A5A5',
        'OUTROS': '#AFAFAF', 'API': '#A9A9A9', 'FILTROS': '#001900', 'CHAMADOS': '#3B75FF',
        'IMPORT / EXPORT': '#A6A6A6', 'LANCAMENTOS': '#BE6A6A', 'CALENDARIO': '#D0D0D0',
        'ADM': '#EAEAEA', 'COMUNICADOS': '#F0F0F0'
    }

    labels = [area.title() for area in area_counts.index]
    colors = [cores_personalizadas.get(area.upper(), '#999999') for area in area_counts.index]

    # Gráfico de Barras
    fig1, ax1 = plt.subplots(figsize=(12, 7))
    bars = ax1.barh(labels, area_counts.values, color=colors)
    ax1.set_title("Quantidade de Registros por Área", fontsize=16, fontweight='bold')
    ax1.set_xlabel("Quantidade")
    ax1.set_ylabel("Área")
    for i, v in enumerate(area_counts.values):
        ax1.text(v + 0.5, i, str(v), va='center', fontsize=8)

    # Gráfico de Pizza
    fig2, ax2 = plt.subplots(figsize=(8, 8))
    wedges, texts, autotexts = ax2.pie(
        area_counts.values,
        labels=labels,
        colors=colors,
        autopct='%1.1f%%',
        startangle=140,
        pctdistance=0.85,
        textprops={'fontsize': 10}
    )
    ax2.set_title("Distribuição Percentual por Área", fontsize=16, fontweight='bold')

    # Mostrar os gráficos
    st.pyplot(fig1)
    st.pyplot(fig2)
else:
    st.info("👆 Envie um arquivo Excel com a coluna 'definicao_area' para gerar os gráficos.")
