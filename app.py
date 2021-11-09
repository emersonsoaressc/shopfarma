from tkinter import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import os

app = Tk()

def produto_pp(ean_medicamento):
    try:
        driver = webdriver.Chrome()
        driver.implicitly_wait(0.5)
        driver.get(f'https://www.precopopular.com.br/#&search-term={ean_medicamento}')
        medicamento = f'{ean_medicamento}'
        driver.find_element_by_class_name("product-item__img__default").click()
        preco_pp = driver.find_element_by_class_name("skuBestPrice")
        preco_pp = preco_pp.text
        driver.quit()
        return preco_pp
    except:
        driver.quit()
        preco_pp = "Nenhum produto encontrado!"
        return preco_pp


def priceAnalyser():
    preco_pp = produto_pp(ean_entry.get())
    print(f'{preco_pp}')
    return preco_pp


app.title("Comparador de Preços")
app.geometry("500x300")
app.configure(background= '#E0FFFF')
preco_pp = ''

#Entrada de texto - Código de barras
Label(app, text='Código de barras do produto:', background='#E0FFFF', foreground='#009', anchor=W).place(x=10, y=10, width=300, height=20)
ean_entry = Entry(app)
ean_entry.place(x=10, y=40, width=200, height=25)

#Botão de ativação do script que rastreia o produto nos sites dos concorrentes
Button(app, text='Consultar', command=priceAnalyser).place(x=10, y=90, width=100, height=30)

Label(app, text=f'{preco_pp}', background='#E0FFFF', foreground='#009', anchor=W).place(x=10, y=10, width=300, height=20)


app.mainloop()
