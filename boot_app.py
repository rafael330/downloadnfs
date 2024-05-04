import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')
st.title('DOWNLOAD DE NFS')

col1, col2 = st.columns(2)

with col1:    
    text_nf = st.text_input('Pedios para baixar NFs','Inclua aqui os pedidos')
    lista_nfs = [[nf.strip(), ''] for nf in text_nf.split(' ')]
    lista_df = pd.DataFrame(lista_nfs, columns=['NFs','STATUS'])
with col2:
    st.markdown("""
    <style>
    div.stButton > button:first-child {
        margin: auto;
        display: block;
    }
    </style>""", unsafe_allow_html=True)
    
    def app_download():
        import pyautogui as py
        import pandas as pd
        import time
        from selenium import webdriver
        from selenium.webdriver.common.keys import Keys
        from selenium.webdriver.common.by import By
        
        navegador = webdriver.Chrome()
        navegador.get("https://sandiego.magazineluiza.com.br/login?redirect=https%3A%2F%2Fsandiego.magazineluiza.com.br%2F")
        navegador.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/form/div[1]/div/input').send_keys("CLR_FERREIRA")
        navegador.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/form/div[2]/div/input').send_keys("Jamilly2010")
        navegador.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/form/div[2]/div/input').send_keys(Keys.ENTER)
        py.hotkey('winleft','up')
        time.sleep(3)

        
        for index, row in lista_df.iterrows():
            nome = row['NFs']
            navegador.get(f'https://sandiego.magazineluiza.com.br/pedidos?suborders.id={nome}')
            time.sleep(5)  
            navegador.find_element(By.XPATH, '/html/body/div/div[2]/div[3]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[2]/button').click()
            time.sleep(5)        
            navegador.find_element(By.XPATH, '/html/body/div/div[2]/div[3]/div/div[3]/div[1]/div/div/button[2]').click()
            time.sleep(5)
        
            try:
                navegador.find_element(By.XPATH, '/html/body/div/div[2]/div[3]/div/div[3]/div[2]/div/div[2]/div[3]/div/a').click()
                time.sleep(3)
            
                py.click(1250,143)        
                time.sleep(2)
                py.write(f'{nome}')
                py.press('enter')
                py.click(240,404)
                lista_df.at[index, 'STATUS'] = 'BAIXADO'
                lista_df.to_excel('TESTE_NF_teste.xlsx', index=False)
                continue

            except:
                lista_df.at[index, 'STATUS'] = 'NÃO BAIXADO'
                lista_df.to_excel('TESTE_NF_teste.xlsx', index=False)

        lista_df.to_excel('TESTE_NF_teste.xlsx', index=False)
        py.alert('FINALIZADO')
    
    botao = st.button('Iniciar downloads', type='primary')
    if botao:
        app_download()
