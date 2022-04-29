from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from tkinter import *
from time import sleep
import os
import shutil

# EMAIL E SENHA
EMAIL = '..escreva aqui..'
SENHA = '..escreva aqui..'

clientes = ['MERCADINHO LTDA', 'MERCADINHO LTDA 2', 'CLIENTE 3']

win = Tk()

win.geometry("700x350")

lb = Listbox(win, width=100, height=10, font=('Times 13'), selectbackground="black", selectmode='multiple')
lb.pack()

def selecionados():
    for i in lb.curselection():
        x = len(str(i))
        while x > 0:
            print(lb.get(i))

            options = webdriver.ChromeOptions()
            options.add_experimental_option('prefs', {
            "plugins.always_open_pdf_externally": True #pra n aparecer a tela do pdf
            })

            driver = webdriver.Chrome(options=options)
            driver.get('https://auditore.herokuapp.com/users/sign_in')

            # Logar no auditore

            driver.find_element_by_xpath('//*[@id="user_email"]').send_keys(EMAIL)
            driver.find_element_by_xpath('//*[@id="user_password"]').send_keys(SENHA)
            driver.find_element_by_xpath('//*[@id="new_user"]/input[3]').click()

            #Pesquisar cliente

            driver.find_element_by_xpath('//*[@id="autocomplete"]/input[1]').click()
            driver.find_element_by_xpath('//*[@id="autocomplete"]/input[1]').send_keys((lb.get(i)))

            sleep(1)
            driver.find_element_by_link_text(lb.get(i)).click()

            #Clicar em data do recebimento

            sleep(1)
            driver.find_element_by_xpath('/html/body/div/div/div/div/div/div[2]/div/div[2]/label[2]').click()


            # Clicar em imprimir
            sleep(1)
            driver.find_element_by_xpath('/html/body/div/div/div/div/div/div[5]/div[1]/a[1]').click()
            sleep(4)
                                                # user do seu pc
            file_oldname = os.path.join("C:\\Users\\SEU USER AQUI\\Downloads\\", "lots_report.pdf")
            strclt = str(lb.get(i))
                                                        # user do seu pc
            file_newname_newfile = os.path.join("C:\\Users\\SEU USER AQUI\\Downloads\\", strclt + ".pdf")
            os.rename(file_oldname, file_newname_newfile)
                              # user do seu pc
            source = 'C:/Users/SEU USER AQUI/Downloads/'+strclt+'.pdf'
            destination = 'C:/Users/SEU USER AQUI/Desktop/'+strclt+'.pdf'

            source = str(source)
            destination = str(destination)

            shutil.move(source, destination)
            
            x -= 1

           

        else:
            print('Erro, tente novamente')


for cliente in clientes:
    lb.insert('end', cliente)

Button(win, text="Confirmar", command=selecionados).pack()

win.mainloop()