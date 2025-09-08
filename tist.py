from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import numpy
import pandas as pd
from selenium.webdriver.common.keys import Keys
import os
from PIL import Image

hapit = pd.read_excel("Mailing Agosto.xlsx")
hapit ['CELULAR_CONTATO_PRINCIPAL_SFA'] = hapit['CELULAR_CONTATO_PRINCIPAL_SFA'].apply(lambda x: f'{x:.0f}')


hapit['NR_CNPJ'] = hapit['NR_CNPJ'].astype(str).str.zfill(14)
eliminados = hapit.loc[(hapit['SEMAFORO_SERASA'] != 'PRETO') & (hapit['SEMAFORO_SERASA'] != 'CINZA') & (hapit['SEMAFORO_SERASA'] != 'N/A') & (hapit['VALOR'] > 1) ]
col_envi = eliminados.loc[hapit['SITUACAO_RECEITA'] == '2 - ATIVA',['NR_CNPJ', 'NM_CLIENTE', 'CELULAR_CONTATO_PRINCIPAL_SFA', 'SITUACAO_RECEITA', 'MENSAGEM_RETORNO_SERASA', 'VALOR']]
print(col_envi['VALOR'])