import streamlit as st
import pandas as pd
import time
import plotly.graph_objects as go

st.markdown("# Análise de preços dos combustiveis")


#VARIAÇÃO DO PREÇO DA GASOLINA
df1 = pd.read_csv('Pages/gasolina_2000+.csv')
df2 = pd.read_csv('Pages/gasolina_2010+.csv')
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
    
    return fig.show()

if st.sidebar.checkbox('Exibir barra de pesquisa'):
    ano=st.sidebar.slider('Defina o ano', min_value=2004,max_value=2021)
    st.text_input('Produto', key='name_produto')
    produto_input=st.session_state.name_produto
    df_grafico = df[(df['PRODUTO']==produto_input)]
    st.line_chart(gera_grafico_din(produto_input, ano))
else:    
    opcao=st.sidebar.selectbox(
        'Selecione o produto',
        df_produtos.drop_duplicates()
    )
    ano=st.sidebar.slider('Defina o ano', min_value=2004,max_value=2021)
    df=gera_grafico_din(opcao,ano)
    st.line_chart(df)
    gera_histograma(df,opcao,ano)
    

