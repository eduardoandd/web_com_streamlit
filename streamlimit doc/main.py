import streamlit as st
import pandas as pd
import numpy as np
import time

# df=pd.DataFrame({
#     'first column':[1,2,3,4],
#     'second column':[10,0,30,40]
# })
# df
# st.text('teste')
# st.table(df)

# #GERANDO DADOS ALEATORIOS COM NUMPY
# dataframe= np.random.randn(10,20)
# st.dataframe(dataframe)

# dataframe_2 =pd.DataFrame(
#     dataframe,
#     columns=('col %d' % i for i in range(20))
# )
# #COLORINDO AS LINHAS COM MAIORES NÚMEROS
# st.dataframe(dataframe_2.style.highlight_max(axis=0))

# #TABELA ESTÁTICA
# st.table(dataframe)

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

opcao = st.sidebar.selectbox(
    'Selecione o Produto',
    df_produtos.drop_duplicates()
)

df_grafico = df[(df['PRODUTO']==opcao)]
df_grafico=df_grafico[['PRODUTO','ANO/MES','PREÇO MÉDIO REVENDA']]
type(df.iloc[1,-1])
# df_grafico['ANO/MES']=pd.to_datetime(df_grafico['ANO/MES'], format='%m-%Y')
df_grafico=df_grafico.groupby('ANO/MES')[['PREÇO MÉDIO REVENDA']].mean()

#PEGANDO APENAS OS VALORES DOS MESES DE SELECIONADOS
x=st.sidebar.slider('Defina o ano', min_value=2000,max_value=2021)
mes_df_grafico_2020=df_grafico[df_grafico.index.year==x]
mes_df_grafico_2020['MES 2020'] = mes_df_grafico_2020.index.month
mes_df_grafico_2020.set_index('MES 2020', inplace=True)
# st.line_chart(mes_df_grafico_2020)

# df_grafico_2020= df_grafico
# df_grafico_2020['MES']=df_grafico_2020.index.month
# df_grafico_2020.reset_index(inplace=True)
# df_grafico_2020.set_index('MES',inplace=True)
# df_grafico_2020=df_grafico_2020['ANO/MES']
# st.line_chart(df_grafico_2020)

#GERANDO GRAFICO PARA OS SEGUINTES DATAFRAMES
#st.line_chart(df_grafico)


#GERANDO MAPA
# map_data = pd.DataFrame(
#     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
#     columns=['lat', 'lon'])

# st.map(map_data)


#WIDGETS
# x=st.slider('x')
# st.write(x, 'ao quadrado é: ',x*x)

#WIDGETS KEY
st.text_input('Seu nome: ', key='name')
st.session_state.name

#CHECKBOX
if st.checkbox('Exibir Data Frame'):
    st.line_chart(mes_df_grafico_2020)
     
#SELECTBOX
# opcao = st.selectbox(
#     'Selecione o Produto',
#     df_grafico.index.year
# )


left_column,right_column=  st.columns(2)

#left_column.button('Pressione')
left_column.button('Pressione')

with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")

ultima_interacao=st.empty()
bar=st.progress(0)

for i in range(100):
    ultima_interacao.text(f'Interação {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)
