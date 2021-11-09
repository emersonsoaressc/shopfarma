import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


cad_prod = pd.read_excel('export/cad_prod_anticoncepcionais.xls', header=13, usecols='C,D,F,K,S,W')
cad_prod = cad_prod.rename({'Reduz. ':'sku', 'Unnamed: 3': 'name','Unnamed: 5':'laboratory','Unnamed: 10':'ean','Unnamed: 18':'depto','Unnamed: 22':'category'}, axis=1)
cad_prod



    
