import streamlit as st
import pandas as pd
import time
import plotly.graph_objects as go

st.markdown("# Análise de preços dos combustiveis")


#VARIAÇÃO DO PREÇO DA GASOLINA
df1 = pd.read_csv('gasolina_2000+.csv')
df2 = pd.read_csv('gasolina_2010+.csv')
df=pd.concat([df1,df2])

pd.to_datetime(df['DATA INICIAL'])
pd.to_datetime(df['DATA FINAL'])                    
df['ANO/MES']=pd.to_datetime(df['DATA FINAL']).dt.strftime('%m-%Y')
df['ANO/MES']=pd.to_datetime(df['ANO/MES'], format='%m-%Y')
type(df.iloc[1,-1])

df_produtos=df[['PRODUTO']]

@st.cache_data
def gera_grafico_din(opcao,ano):
    df_grafico = df[(df['PRODUTO']==opcao)]
    df_grafico=df_grafico[['PRODUTO','ANO/MES','PREÇO MÉDIO REVENDA']]
    type(df.iloc[1,-1])
    df_grafico=df_grafico.groupby('ANO/MES')[['PREÇO MÉDIO REVENDA']].mean()

    #PEGANDO APENAS OS VALORES DOS MESES DE SELECIONADOS
    mes_df_grafico_2020=df_grafico[df_grafico.index.year==ano]
    mes_df_grafico_2020['MES 2020'] = mes_df_grafico_2020.index.month
    mes_df_grafico_2020.set_index('MES 2020', inplace=True)
    
    return mes_df_grafico_2020

def gera_histograma(df,opcao,ano):
    df = gera_grafico_din(opcao,ano)
    fig = go.Figure(data=[go.Histogram(x=df['PREÇO MÉDIO REVENDA'], marker=dict(color='Orange'))])
    fig.update_layout(
        title=f'Variação de preço do(a) {opcao} no ano de {ano}',
        xaxis_title='Valores',
        yaxis_title='Frequência',
    )
    
    return fig.show()

def gera_heatmap(ano,opcao):
    df_gasolina=df[df['PRODUTO']==opcao]
    df_gasolina.set_index('ANO/MES',inplace=True)
    
    df_gasolina=df_gasolina[df_gasolina.index.year==ano]
    df_gasolina.index=df_gasolina.index.month
    
    colorscale_custom = [
        [0, 'rgb(0, 0, 255)'],     # Azul para valores próximos a 0
        [0.5, 'rgb(255, 255, 255)'], # Branco para valores intermediários
        [1, 'rgb(255, 0, 0)']      # Vermelho para valores próximos a 1
    ]
    
    fig_heatmap=go.Figure(data=go.Heatmap(
        z=df_gasolina['PREÇO MÉDIO REVENDA'],
        x=df_gasolina['ESTADO'],
        y=df_gasolina.index,
        colorscale=colorscale_custom  
    ))
    
    fig_heatmap.update_layout(
        plot_bgcolor= '#262730',      # Fundo preto
        paper_bgcolor='#262730',     # Fundo do gráfico preto
        font=dict(color='#527B9D',size=9)   # Texto em branco
    )
    
    return fig_heatmap.show()

if st.sidebar.checkbox('Exibir barra de pesquisa'):
    ano=st.sidebar.slider('Defina o ano', min_value=2004,max_value=2021)
    st.text_input('Produto', key='name_produto')
    produto_input=st.session_state.name_produto
    df_grafico = df[(df['PRODUTO']==produto_input)]
    st.line_chart(gera_grafico_din(produto_input, ano))
else:    
    opcao=st.sidebar.selectbox(
        'Selecione o produto',
        placeholder='tester',
        options=df_produtos.drop_duplicates(),
    )
    ano=st.sidebar.slider('Defina o ano', min_value=2004,max_value=2021)
    df_=gera_grafico_din(opcao,ano)
    st.line_chart(df_)
    if st.sidebar.button('Gerar Histograma', type='primary'):
        status_carregamento=st.text("Gerando Histogama..")
        gera_histograma(df_,opcao,ano)
        status_carregamento.text('Histograma gerado com sucesso!')
    
    if st.sidebar.button('Gerar HeatMap', type='primary'):
        status_carregamento=st.text("Gerando HeatMap..")
        gera_heatmap(ano,opcao)
        status_carregamento.text('HeatMap gerado com sucesso!')
    

