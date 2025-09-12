from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import numpy
import pandas as pd
from selenium.webdriver import Keys



hapit = pd.read_excel("Mailing Agosto.xlsx")
hapit ['CELULAR_CONTATO_PRINCIPAL_SFA'] = hapit['CELULAR_CONTATO_PRINCIPAL_SFA'].apply(lambda x: f'{x:.0f}')
hapit ['TLFN_1'] = hapit['TLFN_1'].apply(lambda x: f'{x:.0f}')
hapit ['TLFN_2'] = hapit['TLFN_2'].apply(lambda x: f'{x:.0f}')
hapit ['TLFN_3'] = hapit['TLFN_3'].apply(lambda x: f'{x:.0f}')
hapit ['TLFN_4'] = hapit['TLFN_4'].apply(lambda x: f'{x:.0f}')
hapit ['TLFN_5'] = hapit['TLFN_5'].apply(lambda x: f'{x:.0f}')
hapit ['TEL_COMERCIAL_SIEBEL'] = hapit['TEL_COMERCIAL_SIEBEL'].apply(lambda x: f'{x:.0f}') 
hapit ['TEL_CELULAR_SIEBEL'] = hapit['TEL_CELULAR_SIEBEL'].apply(lambda x: f'{x:.0f}')
hapit ['TEL_RESIDENCIAL_SIEBEL'] = hapit['TEL_RESIDENCIAL_SIEBEL'].apply(lambda x: f'{x:.0f}')
hapit['NR_CNPJ'] = hapit['NR_CNPJ'].astype(str).str.zfill(14)
eliminados = hapit.loc[(hapit['SEMAFORO_SERASA'] != 'PRETO') & (hapit['SEMAFORO_SERASA'] != 'CINZA') & (hapit['SEMAFORO_SERASA'] != 'N/A') & (hapit['VALOR'] > 1) ]
col_envi = eliminados.loc[hapit['SITUACAO_RECEITA'] == '2 - ATIVA',['NR_CNPJ', 'NM_CLIENTE', 'CELULAR_CONTATO_PRINCIPAL_SFA', 'TLFN_1', 'TLFN_2', 'TLFN_3', 'TLFN_4', 'TLFN_5', 'TEL_COMERCIAL_SIEBEL', 'TEL_CELULAR_SIEBEL', 'TEL_RESIDENCIAL_SIEBEL', 'SITUACAO_RECEITA', 'MENSAGEM_RETORNO_SERASA', 'VALOR']]
print(col_envi['VALOR'])

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
   time.sleep(1)
   textbox = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[3]/div/div[3]/header/header/div/span/div/div[1]/span/div/div/div[1]/div[1]/span')
   
   
   time.sleep(4)
   if len(driver.find_elements(By.XPATH, '//*[@id="app"]/div[1]/div[3]/div/div[2]/div[1]/span/div/span/div/div[1]/div[2]/span')) == 0:
      textbox.click()
  
   textbox = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[3]/div/div[2]/div[1]/span/div/span/div/div[1]/div[2]/div/div/div[1]/p')#1
   textbox.send_keys(col_envi['CELULAR_CONTATO_PRINCIPAL_SFA'])
   textbox.click()
   time.sleep(2)
   i = 1
   
   if len(driver.find_elements(By.XPATH, '//*[@id="app"]/div[1]/div[3]/div/div[2]/div[1]/span/div/span/div/div[2]/div[3]/div[1]')) < 1 or len(driver.find_elements(By.XPATH, '//*[@id="app"]/div[1]/div[3]/div/div[2]/div[1]/span/div/span/div/div[2]/div[3]')) < 1:
      veri = 1
      textbox.send_keys(Keys.CONTROL, Keys.BACKSPACE)
      textbox.send_keys(col_envi['TLFN_1'])
      time.sleep(3)      
      try:
         teste = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[3]/div/div[2]/div[1]/span/div/span/div/div[2]/div[3]')
         teste.click()
         veri + 1
      except:
         pass
      if veri == 2:
         pass
         textbox.send_keys(col_envi['TLFN_2'])
         time.sleep(2)
         try:
            teste = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[3]/div/div[2]/div[1]/span/div/span/div/div[2]/div[3]')
            teste.click()
         except:
            pass
      if veri == 2:
         pass
         textbox.send_keys(col_envi['TLFN_3'])
         time.sleep(2)
         try:
            teste = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[3]/div/div[2]/div[1]/span/div/span/div/div[2]/div[3]')
            teste.click()
         except:
            pass
      if veri == 2:
         textbox.send_keys(Keys.CONTROL, Keys.BACKSPACE)
         textbox.send_keys(col_envi['TLFN_4'])
         time.sleep(3)
         try:
            teste = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[3]/div/div[2]/div[1]/span/div/span/div/div[2]/div[3]')
            teste.click()
         except:
            pass
      if veri == 2:
         textbox.send_keys(Keys.CONTROL, Keys.BACKSPACE)
         textbox.send_keys(col_envi['TLFN_5'])
         time.sleep(2)
         try:
            teste = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[3]/div/div[2]/div[1]/span/div/span/div/div[2]/div[3]')
            teste.click()
         except:
            pass
      if veri == 2:
         textbox.send_keys(Keys.CONTROL, Keys.BACKSPACE)
         textbox.send_keys(col_envi['TEL_COMERCIAL_SIEBEL'])
         time.sleep(3)
         try:
            teste = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[3]/div/div[2]/div[1]/span/div/span/div/div[2]/div[3]')
            teste.click()
         except:
            pass
      if veri == 2:
         textbox.send_keys(Keys.CONTROL, Keys.BACKSPACE)
         textbox.send_keys(col_envi['TEL_CELULAR_SIEBEL'])
         time.sleep(2)
         try:
            teste = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[3]/div/div[2]/div[1]/span/div/span/div/div[2]/div[3]')
            teste.click()
         except:
            pass
      if veri == 2:
         textbox.send_keys(Keys.CONTROL, Keys.BACKSPACE)
         textbox.send_keys(col_envi['TEL_RESIDENCIAL_SIEBEL'])
         try:
            teste = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[3]/div/div[2]/div[1]/span/div/span/div/div[2]/div[3]')
            teste.click()
         except:
            pass
   
   try:
      chat = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[3]/div/div[2]/div[1]/span/div/span/div/div[2]/div[3]/div[2]')
      chat.click()
   except:
      pass
   try:
      teste = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[3]/div/div[2]/div[1]/span/div/span/div/div[2]/div[3]')
      teste.click()
   except:
      pass
   

   i += 1
   if i == 5:
      break
         
   time.sleep(2)
   chatbox = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div/div[3]/div[1]/p')
   chatbox.click()
   time.sleep(2)

   chatbox.send_keys( " *Crédito Aprovado para Você!*  ") #"\u2705"Okayzinho #"\u263A" carinha #"\u21E5" seta #"\u23F3"ampulheta)
   chatbox = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div/div[3]/div[1]/p')
   chatbox.send_keys(Keys.SHIFT + Keys.RETURN)
   chatbox.send_keys(Keys.SHIFT + Keys.RETURN)
   chatbox.send_keys("Olá tudo? " + "\u263A")
   chatbox.send_keys(Keys.SHIFT + Keys.RETURN)
   chatbox.send_keys(f"Você foi pré-aprovado para adquirir seu novo aparelho móvel com crédito de até R$ {col_envi['VALOR']}! Aproveite essa oportunidade exclusiva para sair com o celular dos seus sonhos, com parcelas que cabem no seu bolso!" )
   chatbox.send_keys(Keys.SHIFT + Keys.RETURN)
   chatbox.send_keys(Keys.SHIFT + Keys.RETURN)
   chatbox.send_keys("\u2705" + "Sem burocracia")
   chatbox.send_keys(Keys.SHIFT + Keys.RETURN)
   chatbox.send_keys("\u2705" + "Aprovação rápida")
   chatbox.send_keys(Keys.SHIFT + Keys.RETURN)
   chatbox.send_keys("\u2705" + "Aparelhos 100% novos e com garantia")
   chatbox.send_keys(Keys.SHIFT + Keys.RETURN)
   chatbox.send_keys("\u2705" + "Diversas marcas e modelos disponíveis")
   chatbox.send_keys(Keys.SHIFT + Keys.RETURN)
   chatbox.send_keys(Keys.SHIFT + Keys.RETURN)
   chatbox.send_keys("Nosso time está pronto para te atender e garantir a melhor condição.")
   chatbox.send_keys(Keys.SHIFT + Keys.RETURN)
   chatbox.send_keys("Clique no link abaixo para falar com um consultor agora mesmo:")
   chatbox.send_keys(Keys.SHIFT + Keys.RETURN)
   chatbox.send_keys(Keys.SHIFT + Keys.RETURN)
   chatbox.send_keys("\u21E5" + "link do consultor ")
   chatbox.send_keys(Keys.SHIFT + Keys.RETURN)
   chatbox.send_keys(Keys.SHIFT + Keys.RETURN)
   chatbox.send_keys("Mas corra! Essa condição é por tempo limitado " + "\u23F3")
   chatbox.send_keys(Keys.SHIFT + Keys.RETURN)
   chatbox.send_keys(Keys.SHIFT + Keys.RETURN)
   chatbox.send_keys("SS-Telecom – Tecnologia que te conecta.")
   ent = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div/div[4]')
   ent.click()
   time.sleep(2)
   
   time.sleep(2)
   
   while len(driver.find_elements(By.ID, "side")) < 1:
      time.sleep(3)
   

   # attach = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div/div[1]/div/span/div/div/div[1]/div[1]/span')
   # time.sleep(1)
   # attach.click()
   # catalog = driver.find_element(By. XPATH, '//*[@id="app"]/div[1]/span[6]/div/ul/div/div/div[10]/li')
   # time.sleep(2)
   # catalog.click()
   # time.sleep(5)
   # while len(driver.find_elements(By.XPATH, '//*[@id="app"]/div[1]/span[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div[1]/div/div[2]')) < 1:
   #    time.sleep(3)

   # catalog_Button = driver.find_element(By. XPATH, '//*[@id="app"]/div[1]/span[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div[1]/div/div[2]')
   # catalog_Button.click()
   # time.sleep(3)
   # catalog_B_envi1 = driver.find_element(By. XPATH, '//*[@id="app"]/div[1]/span[2]/div/div/div/div/div/div/div/span/div/div') 
   # catalog_B_envi1.click()
   







