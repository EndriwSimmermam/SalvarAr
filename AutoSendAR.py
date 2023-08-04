from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from customtkinter import *
from time import sleep
import os

# formulario popup
janela = CTk()
janela.title('Enviador de Aviso de Recebimento')
janela.geometry('400x300')

# numero ar
label_ar = CTkLabel(janela, text='Insira os dados:',
                    font=('Helvetica bold', 20))
label_ar.pack(padx=10, pady=10)
ar_number = CTkEntry(janela, placeholder_text='Número do AR',
                     width=200, font=('Helvetica bold', 14))
ar_number.pack(padx=10, pady=20,)

# nome documento
ar_nome = CTkEntry(janela, placeholder_text='Nome do arquivo',
                   width=200, font=('Helvetica bold', 14))
ar_nome.pack(padx=10, pady=10)


def enviardados(event):
    global ar
    global doc
    ar = ar_number.get()
    doc = ar_nome.get()
    janela.destroy()


# botao de enviar
button = CTkButton(janela, text='ENVIAR', font=(
    'Helvetica bold', 18), command=enviardados)
button.bind('<Button-1>', enviardados)
button.pack(padx=40, pady=20)


janela.bind('<Return>', enviardados)
janela.mainloop()

# entrando no navegador
driver = webdriver.Edge()

sleep(2)

driver.get(
    'http://vcremona/Ripplestone/SignOn.aspx?ReturnUrl=%2fripplestone%2fHome.aspx')

# entrando com usuario
usuario = webdriver.find_element(By.XPATH, 'txtUserID')
usuario.send_keys('endriw')

senha = webdriver.find_element(By.XPATH, 'txtPassword')
senha.send_keys('123')

button_login = webdriver.find_element(By.XPATH, 'btnLogin').click()

# abrindo caixa de pesquisa ar
ar_link = webdriver.find_element(
    By.XPATH, 'ctl00_MainContent_ASPxPageControl1_panelMyDocuments_repeaterFavorites_ctl01_lnkbtnRunFav').click()

ar_box = webdriver.find_element(By.XPATH, 'pePromptTextBox').click()
ar_box.send_keys(f'{ar}')

btn_ok = webdriver.find_element(By.XPATH, 'pePromptButton').click()

sleep(60)

# exportando o ar
ar_export = webdriver.find_element(
    By.XPATH, 'IconImg_CrystalReportViewer1_toptoolbar_export').click()
ar_export2 = webdriver.find_element(By.XPATH, 'wizbutton').click()

sleep(2)

# fechar o navegador
driver.quit()
