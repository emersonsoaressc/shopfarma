import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


cad_prod = pd.read_excel('export/cad_prod_anticoncepcionais.xls', header=13, usecols='C,D,F,K,S,W')
cad_prod = cad_prod.rename({'Reduz. ':'sku', 'Unnamed: 3': 'name','Unnamed: 5':'laboratory','Unnamed: 10':'ean','Unnamed: 18':'depto','Unnamed: 22':'category'}, axis=1)
cad_prod

def descobre_cod_concorrentes(ean_produto):
    driver = webdriver.Chrome()
    driver.implicitly_wait(0.2)
    driver.get(f'https://www.cliquefarma.com.br/preco/{ean_produto}')
    elems = driver.find_elements_by_css_selector(".block-oferta [href]")
    links = [elem.get_attribute('href') for elem in elems]
    driver.quit()
    
    # Código Panvel - 23
    for i in links:
        if (f'empresa=23') in i:
            link_panvel = i
            codigo_panvel = (link_panvel.split('&',1)[0]).split('=',1)[1]
            break
    # Código PP - 184
    for i in links:
        if (f'empresa=184') in i:
            codigo_pp = ''
            link_pp = i
            pp = webdriver.Chrome()
            pp.implicitly_wait(0.5)
            pp.get(f'{link_pp}')
            pp_elements = pp.find_elements_by_tag_name("div")
            for element in pp_elements:
                if 'productReference' in element.get_attribute('class'):
                    codigo_pp = element.text
                    pp.quit()
                    return codigo_pp
            break
    # Código Raia - 28
    for i in links:
        if (f'empresa=28') in i:
            link_raia = i
            codigo_raia = (link_raia.split('&',1)[0]).split('=',1)[1]
            break
    return codigo_panvel, codigo_pp, codigo_raia

    
