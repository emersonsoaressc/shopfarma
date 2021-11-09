import pandas as pd
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
chrome_options = Options()
chrome_options.add_argument("--headless")


def cod_concorrentes(ean_produto):
    try:
        driver = webdriver.Chrome(options=chrome_options)
        driver.implicitly_wait(0.2)
        driver.get(f'https://www.cliquefarma.com.br/preco/{ean_produto}')
        elems = driver.find_elements_by_css_selector(".block-oferta [href]")
        links = [elem.get_attribute('href') for elem in elems]
        driver.quit()
        codigo_panvel = ''
        codigo_raia = ''
        codigo_pp = ''
        codigo_paguemenos = ''
    except:
        print('Nenhum produto encontrado')
    
    # Código Panvel - 23
    try:
        for i in links:
            if (f'empresa=23&') in i:
                link_panvel = i
                codigo_panvel = (link_panvel.split('&',1)[0]).split('=',1)[1]
                break
    except:
        print('Produto não encontrado!')

    # Código Raia - 28
    try:
        for i in links:
            if (f'empresa=28&') in i:
                link_raia = i
                codigo_raia = (link_raia.split('&',1)[0]).split('=',1)[1]
                break
    except:
        print('Produto não encontrado!')

    # Código PP
    try:
        for i in links:
            if (f'empresa=184&') in i:
                codigo_pp = ''
                link_pp = i
                pp = webdriver.Chrome(options=chrome_options)
                pp.implicitly_wait(0.5)
                pp.get(f'{link_pp}')
                sleep(2)
                pp_element = pp.find_element_by_css_selector(".productReference")
                codigo_pp = pp_element.text
                pp.quit()
                """
                pp_elements = pp.find_elements_by_css_selector(".productReference")
                for element in pp_elements:
                    if 'productReference' in element.get_attribute('class'):
                        codigo_pp = element.text
                        pp.quit()
                """
    except:
        print('Produto não encontrado!')

    # Código Pague Menos
    try:
        paguemenos = webdriver.Chrome(options=chrome_options)
        paguemenos.implicitly_wait(0.5)
        paguemenos.get(f'https://www.paguemenos.com.br/{ean_produto}')
        sleep(2)
        paguemenos_element_box = paguemenos.find_element_by_class_name("vtex-product-summary-2-x-imageContainer")
        paguemenos_element_box.click()
        sleep(2)
        paguemenos_element = paguemenos.find_element_by_class_name('vtex-product-identifier-0-x-product-identifier__value')
        codigo_paguemenos = paguemenos_element.text
    except:
        print('Produto não encontrado!')

    return codigo_panvel, codigo_raia, codigo_pp, codigo_paguemenos