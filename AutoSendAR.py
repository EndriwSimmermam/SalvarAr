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

strarnomedoc = (f'{ar} - {doc}.pdf')

# entrando no navegador
driver = webdriver.Edge()

sleep(2)

driver.get('http://vcremona/Ripplestone/SignOn.aspx?ReturnUrl=%2fripplestone%2fHome.aspx')

# entrando com usuario
usuario = driver.find_element(By.XPATH, '/html/body/form/div[3]/div[2]/div[2]/table/tbody/tr[1]/td/table/tbody/tr[1]/td[2]/input')
usuario.send_keys('endriw')

senha = driver.find_element(By.XPATH, '/html/body/form/div[3]/div[2]/div[2]/table/tbody/tr[1]/td/table/tbody/tr[2]/td[2]/input')
senha.send_keys('123')

button_login = driver.find_element(By.XPATH, '/html/body/form/div[3]/div[2]/div[2]/table/tbody/tr[1]/td/table/tbody/tr[3]/td/input').click()

# abrindo caixa de pesquisa ar
ar_link = driver.find_element(By.XPATH, '/html/body/form/div[3]/div[3]/div[4]/div/div/div/div[2]/div[2]/table/tbody/tr[2]/td/div/div/table/tbody/tr[1]/td[2]/a').click()

ar_box = driver.find_element(By.XPATH, '/html/body/table/tbody/tr/td/table/tbody/tr[2]/td/div/form/div/div/fieldset/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr[2]/td[1]/input').click()
ar_box.send_keys(f'{ar}')

btn_ok = driver.find_element(By.XPATH, '/html/body/table[1]/tbody/tr/td/table/tbody/tr[2]/td/div/form/div/div/table/tbody/tr/td/table/tbody/tr/td[2]/div/a').click()

sleep(30)

# exportando o ar
ar_export = driver.find_element(By.XPATH, '/html/body/form/div[3]/div[3]/div[4]/div/div/div/div/div[4]/div/div[1]/table/tbody/tr/td[1]/table/tbody/tr/td[1]/table/tbody/tr/td[2]/table/tbody/tr/td[1]/table/tbody/tr/td[5]/table/tbody/tr/td/div/img').click()
ar_export2 = driver.find_element(By.XPATH, '/html/body/table[3]/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr/td[2]/nobr/a').click()

sleep(2)

# fechar o navegador
driver.quit()

os.rename('C:\Users\endriw\Downloads\CrystalReportViewer1.pdf', f'R:\Almoxarifado\Arquivos Comuns\AA - ARs de Compra Direta\ARs de 2023\{strarnomedoc}')

os.startfile("outlook")
