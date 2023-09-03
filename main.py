import streamlit as st
import pandas as pd

st.set_page_config(
    layout='wide',
    page_title='Análise de celulares'
)

df=pd.read_csv('smartphone_cleaned_v5.csv')
# df_exynos=df[(df['processor_brand']=='exynos')]



# st.write(df_exynos[['price','model']].sort_values(by='price',ascending=False))

# st.write(df[['brand_name','price','model']].sort_values(by='price',ascending=False))

# df2 = df
# df2.set_index('price', inplace=True)
# st.line_chart(df2['brand_name'].sort_values(ascending=False))

# df.set_index('model', inplace=True)
# st.line_chart(df[df['battery_capacity'] > 5000]['battery_capacity'])


#QUANTIDADE DE CELULARES DE CADA MARCA
#df.reset_index(inplace=True)
#st.bar_chart(df['brand_name'].value_counts().sort_values(ascending=True))

#QUANTIDADE DE MEMORIA RAM POR CELULAR
#df.reset_index(inplace=True)


#FILTRANDO POR MARCA 
marcas = df['brand_name'].value_counts().index
marca = st.selectbox('Marca', sorted(marcas))
filtro_marca = df[df['brand_name']==marca]

#FILTRANDO POR MARCA E PREÇO
precos = filtro_marca['price'].value_counts().index
preco = st.selectbox('Preço',sorted(precos))
filtro_preco = df[(df['price']==preco) & (df['brand_name']==marca)]


exibir_grafico = st.checkbox('Exibir gráfico')
if exibir_grafico:  
    filtro_preco.set_index('model', inplace=True)
    st.bar_chart(filtro_preco['price'])




