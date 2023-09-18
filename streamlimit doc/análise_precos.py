import streamlit as st
import pandas as pd
import time


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

opcao=st.sidebar.selectbox(
    'Selecione o produto',
    df_produtos.drop_duplicates()
)

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


ano=st.sidebar.slider('Defina o ano', min_value=2000,max_value=2021)
#gera_grafico_din(opcao)

st.text_input('Produto', key='name_produto')
produto_input=st.session_state.name_produto


if st.sidebar.checkbox('Exibir barra de pesquisa'):
    df_grafico = df[(df['PRODUTO']==produto_input)]
    st.line_chart(gera_grafico_din(produto_input, ano))
else:
    st.line_chart(gera_grafico_din(opcao,ano))



