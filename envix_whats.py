from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import numpy
import pandas as pd
from selenium.webdriver.common.keys import Keys
import os
import heapq
from tkinter import filedialog


def escolherArquivo():
    arq_path = filedialog.askopenfilename()
    
    hapit = pd.read_excel(arq_path)
    # hapit ['CELULAR_CONTATO_PRINCIPAL_SFA'] = hapit['CELULAR_CONTATO_PRINCIPAL_SFA'].apply(lambda x: f'{x:.0f}')
    # hapit ['TLFN_1'] = hapit['TLFN_1'].apply(lambda x: f'{x:.0f}')
    # hapit ['TLFN_2'] = hapit['TLFN_2'].apply(lambda x: f'{x:.0f}')
    # hapit ['TLFN_3'] = hapit['TLFN_3'].apply(lambda x: f'{x:.0f}')
    # hapit ['TLFN_4'] = hapit['TLFN_4'].apply(lambda x: f'{x:.0f}')
    # hapit ['TLFN_5'] = hapit['TLFN_5'].apply(lambda x: f'{x:.0f}')
    # hapit ['TEL_COMERCIAL_SIEBEL'] = hapit['TEL_COMERCIAL_SIEBEL'].apply(lambda x: f'{x:.0f}') 
    # hapit ['TEL_CELULAR_SIEBEL'] = hapit['TEL_CELULAR_SIEBEL'].apply(lambda x: f'{x:.0f}')
    # hapit ['TEL_RESIDENCIAL_SIEBEL'] = hapit['TEL_RESIDENCIAL_SIEBEL'].apply(lambda x: f'{x:.0f}')

    col_envi = hapit.loc[hapit ['STATUS'] == 'Ativo', ['CNPJ', 'RAZÃO SOCIAL', 'CONTA', 'Contato', 'E-mail', 'CONSU', 'Email_consu', 'Tipo']]
    print(col_envi)


def start_whats():
    print('Foi')
    driver = webdriver.Chrome()
    driver.get("https://web.whatsapp.com/")
    driver.maximize_window()
    print('oo')

    while len(driver.find_elements(By.ID, "side")) < 1:
        time.sleep(1)

    try:
        adicion = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div/div[3]/header/header/div/span/div/div[1]/button')
        adicion.click()
    except:
        pass
    textbox = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div[1]/span/div/span/div/div[1]/div[2]/div/div/div[1]/p')
    time.sleep(1)
    textbox.click()
    textbox.send_keys('91985747028')
    time.sleep(2)

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

    ent = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div/div[4]/button')
    ent.click()
