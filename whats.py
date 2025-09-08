from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import numpy
import pandas as pd
from selenium.webdriver.common.keys import Keys
import os
from PIL import Image


hapit = pd.read_excel("teste mala.xlsx")
hapit ['CELULAR_CONTATO_PRINCIPAL_SFA'] = hapit['CELULAR_CONTATO_PRINCIPAL_SFA'].apply(lambda x: f'{x:.0f}')
hapit ['TLFN_1'] = hapit['TLFN_1'].apply(lambda x: f'{x:.0f}')
hapit ['TLFN_2'] = hapit['TLFN_2'].apply(lambda x: f'{x:.0f}')
hapit ['TLFN_3'] = hapit['TLFN_3'].apply(lambda x: f'{x:.0f}')
hapit ['TLFN_4'] = hapit['TLFN_4'].apply(lambda x: f'{x:.0f}')
hapit ['TLFN_5'] = hapit['TLFN_5'].apply(lambda x: f'{x:.0f}')
hapit ['TEL_COMERCIAL_SIEBEL'] = hapit['TEL_COMERCIAL_SIEBEL'].apply(lambda x: f'{x:.0f}') 
hapit ['TEL_CELULAR_SIEBEL'] = hapit['TEL_CELULAR_SIEBEL'].apply(lambda x: f'{x:.0f}')
hapit ['TEL_RESIDENCIAL_SIEBEL'] = hapit['TEL_RESIDENCIAL_SIEBEL'].apply(lambda x: f'{x:.0f}')

col_envi = hapit.loc[hapit['SEMAFORO_SERASA'] != 'PRETO', 'CINZA' [
   'NR_CNPJ', 'NM_CLIENTE', 'CELULAR_CONTATO_PRINCIPAL_SFA', 'SITUACAO_RECEITA', 'EMAIL_CONTATO_PRINCIPAL_SFA', 'NM_CONTATO_SFA', 'TLFN_1', 'TLFN_2', 'TLFN_3', 'TLFN_4', 'TLFN_5', 'TEL_COMERCIAL_SIEBEL', 'TEL_CELULAR_SIEBEL', 'TEL_RESIDENCIAL_SIEBEL', 'MENSAGEM_RETORNO_SERASA']]

print(col_envi)

randi = numpy.random.normal(size=(1, 5))
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")
driver.maximize_window()
while len(driver.find_elements(By.ID, "side")) < 1:
   time.sleep(1)


for index, col_envi, in col_envi.iterrows():
   print(col_envi['NM_CLIENTE'])
   try:
      adicion = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div/div[3]/header/header/div/span/div/div[1]/button')
      adicion.click()
   except:
      pass
   textbox = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div[1]/span/div/span/div/div[1]/div[2]/div/div/div[1]/p')
   time.sleep(1)
   textbox.click()
   textbox.send_keys(col_envi['CELULAR_CONTATO_PRINCIPAL_SFA'])
   time.sleep(2)

   i = 1

   while len(driver.find_elements(By.XPATH, '//*[@id="app"]/div[1]/div[3]/div/div[2]/div[1]/span/div/span/div/div[2]/div[3]/div[2]')) < 1:
      ale = numpy.random.randint(2, 5)
      time.sleep(ale)
      textbox.send_keys(Keys.CONTROL, Keys.BACKSPACE)
      textbox.send_keys(col_envi['TLFN_1'])
      time.sleep(ale)
      textbox.send_keys(Keys.CONTROL, Keys.BACKSPACE)
      textbox.send_keys(col_envi['TLFN_2'])
      time.sleep(ale)
      textbox.send_keys(Keys.CONTROL, Keys.BACKSPACE)
      textbox.send_keys(col_envi['TLFN_3'])
      time.sleep(ale)
      textbox.send_keys(Keys.CONTROL, Keys.BACKSPACE)
      textbox.send_keys(col_envi['TLFN_4'])
      time.sleep(ale)
      textbox.send_keys(Keys.CONTROL, Keys.BACKSPACE)
      textbox.send_keys(col_envi['TLFN_5'])
      time.sleep(ale)
      textbox.send_keys(Keys.CONTROL, Keys.BACKSPACE)
      textbox.send_keys(col_envi['TEL_COMERCIAL_SIEBEL'])
      time.sleep(ale)
      textbox.send_keys(Keys.CONTROL, Keys.BACKSPACE)
      textbox.send_keys(col_envi['TEL_CELULAR_SIEBEL'])
      time.sleep(ale)
      textbox.send_keys(Keys.CONTROL, Keys.BACKSPACE)
      textbox.send_keys(col_envi['TEL_RESIDENCIAL_SIEBEL'])
      
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
   
   # attach = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/span[6]/div/ul/div/div/div[1]/li/div/input')
   # time.sleep(2)
   # driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/span[6]/div/ul/div/div/div[1]/li/div/input').send_keys(document1)
   # time.sleep(2)
   # ent = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[3]/div/div[2]/div[2]/span/div/div/div/div[2]/div/div[2]/div[2]/div/div')
   # time.sleep(2)
   enter = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div/div[4]/button')
   # ent.click()






