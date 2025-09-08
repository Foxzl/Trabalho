from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import numpy
import pandas as pd
from selenium.webdriver.common.keys import Keys
import os
from PIL import Image


hapit = pd.read_excel("TESTE.xlsx")
hapit ['NR_TELEFONE'] = hapit['NR_TELEFONE'].apply(lambda x: f'{x:.0f}')


hapit['CNPJ_CLIENTE'] = hapit['CNPJ_CLIENTE'].astype(str).str.zfill(14)
eliminados = hapit.loc[(hapit['ELEGIBILIDADE'] == 'ELEGÍVEL') & (hapit['SEMAFORO_SERASA'] != 'PRETO') & (hapit['SEMAFORO_SERASA'] != 'CINZA') & (hapit['SEMAFORO_SERASA'] != 'N/A') & (hapit['VALOR'] != '')]
col_envi = eliminados.loc[hapit['SITUAÇÃO'] == '2 - ATIVA',['CNPJ_CLIENTE', 'CLIENTE', 'NR_TELEFONE', 'SITUAÇÃO', 'MENSAGEM_RETORNO_SERASA']]
print(col_envi)

for index, col_envi, in col_envi.iterrows():
    print(index)
    alg = bool(col_envi['MENSAGEM_RETORNO_SERASA'] == 'APROVADO ATÉ R$ 1500.00.')
    print(alg)
    if alg:
        print('Sim')
    else:
        print("Não")

randi = numpy.random.normal(size=(1, 5))
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")
driver.maximize_window()
while len(driver.find_elements(By.ID, "side")) < 1:
   time.sleep(1)


for index, col_envi, in col_envi.iterrows():
   print(col_envi['CNPJ_CLIENTE'])
   test = 1
   try:
      adicion = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div/div[3]/header/header/div/span/div/div[1]/button')
      adicion.click()
   except:
      pass
   textbox = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div[1]/span/div/span/div/div[1]/div[2]/div/div/div[1]/p')
   time.sleep(1)
   textbox.click()
   time.sleep(2)

   i = 1

   while len(driver.find_elements(By.XPATH, '//*[@id="app"]/div[1]/div[3]/div/div[2]/div[1]/span/div/span/div/div[2]/div[3]/div[2]')) < 1:
      ale = numpy.random.randint(2, 5)
      time.sleep(ale)
      textbox.send_keys(Keys.CONTROL, Keys.BACKSPACE)
      textbox.send_keys(col_envi['NR_TELEFONE'])
      
      
      i += 1
      if i == 5:
         break
   
  
   chat = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[3]/div/div[2]/div[1]/span/div/span/div/div[2]/div[3]/div[2]')
   chat.click()

   try:
      chat.click()
   except:
      pass
   time.sleep(2)
   chatbox = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div/div[3]/div[1]/p')
   chatbox.click()
   time.sleep(2)
   chatbox.send_keys('Teste!!')
   time.sleep(1)
   
   time.sleep(1)
   
   while len(driver.find_elements(By.ID, "side")) < 1:
      time.sleep(3)
   
   
   document1 = os.getcwd()  + '\\' + 'WHATS\\Card Whatsapp - Antivirus McAfee - PA.png'
   


   attach = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div/div[1]/button')
   time.sleep(1)
   attach.click()
   catalog = driver.find_element(By. XPATH, '//*[@id="app"]/div[1]/span[6]/div/ul/div/div/div[10]/li')
   time.sleep(2)
   catalog.click()
   time.sleep(2)
   catalog_Button = driver.find_element(By. XPATH, '//*[@id="app"]/div[1]/span[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div/div/div[2]')
   catalog_Button.click()
   time.sleep(3)
   catalog_B_envi1 = driver.find_element(By. XPATH, '//*[@id="app"]/div[1]/span[2]/div/div/div/div/div/div/div/span/div/div') 
   catalog_B_envi1.click()
   test =+ 1
   # attach = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/span[6]/div/ul/div/div/div[1]/li/div/input')
   # time.sleep(2)
   # driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/span[6]/div/ul/div/div/div[1]/li/div/input').send_keys(document1)
   # time.sleep(2)
   # ent = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[3]/div/div[2]/div[2]/span/div/div/div/div[2]/div/div[2]/div[2]/div/div')
   # time.sleep(2)
   enter = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div/div[4]/button')
   # ent.click()
