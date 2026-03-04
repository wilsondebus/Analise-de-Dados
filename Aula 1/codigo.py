#cadastrar produtos da base de dados no site da empresa 

#baixar pacote -> pip install pyautogui

#Passo a passo do programa (LÓGICA) 
#1. entrar no sistema da empresa 
#2. fazer o login 
#3. abrir a base de dados 
#4. cadastrar um produto 
#5. repetir passo 4 até acabar a lista de produtos 

import pyautogui  #biblioteca para automatizar tarefas do teclado e mouse 
import time       #biblioteca de controle de tempo 

pyautogui.PAUSE = 0.5   #definir 0.5 seg a cada comando 

#pyautogui.click -> aperta um botão 
#pyautogui.write -> escreva um texto 
#pyautogui.press -> aperta uma tecla 
#pyautogui.hotkey -> aperta um atalho 

link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'    #link do site

#Passo 1:
pyautogui.press('Win')  #abre a janela do windowns 
pyautogui.write('Chrome')   #digita chorme 
pyautogui.press('Enter')  #abre o chrome
pyautogui.write(link)   #escreve o que esta dentro do link
pyautogui.press('Enter')

#fazer uma pausa maior, por conta da internet que pode ser instavel em diferentes situações 
time.sleep(2)   #pede pro computador esperar 3 seg

#Passo 2 (fazer login): 
pyautogui.click(x=-1425, y=373)  #clica na posição da tela
pyautogui.write('seuemail@gmail.com')
pyautogui.press('Tab')  #passa para o proximo campo
pyautogui.write('suaSenha')
pyautogui.press('Enter')

time.sleep(3)

#Passo 3 (abrir a base de dados):
#pip install pandas openpyxl -> biblioteca que trabalha com base de dados (pandas) // (openpyxl) permite o pandas a trabalhar com planilhas do excel
import pandas 

tabelaBaseDeDados = pandas.read_csv('produtos.csv') #vai ler a base de dados e guardar as informações na variavel 

for linha in tabelaBaseDeDados.index:   #para cada linha dentro da tabela 
    #Passo 4 (cadastrar um produto): 
    pyautogui.click(x=-1411, y=260)

    #codigo
    codigo = str(tabelaBaseDeDados.loc[linha, 'codigo'])
    pyautogui.write(codigo)
    pyautogui.press('Tab')

    #marca
    marca = str(tabelaBaseDeDados.loc[linha, 'marca'])
    pyautogui.write(marca)
    pyautogui.press('Tab')

    #tipoLogitech
    tipo = str(tabelaBaseDeDados.loc[linha, 'tipo'])
    pyautogui.write(tipo)
    pyautogui.press('Tab')

    #categoria
    categoria = str(tabelaBaseDeDados.loc[linha, 'categoria'])
    pyautogui.write(categoria)
    pyautogui.press('Tab')

    #preco Unitario 
    preco = str(tabelaBaseDeDados.loc[linha, 'preco_unitario'])
    pyautogui.write(preco)
    pyautogui.press('Tab')

    #custo 
    custo = str(tabelaBaseDeDados.loc[linha, 'custo'])
    pyautogui.write(custo)
    pyautogui.press('Tab')
   
    #obs
    obs = str(tabelaBaseDeDados.loc[linha, 'obs'])
    if obs != 'nan':   
        pyautogui.write(obs) 
    pyautogui.press('Tab')

    pyautogui.press('Enter')       
    #depois de cadastrar eu tenho que voltar pro inicio da tela 
    pyautogui.scroll(5000)  #numero positivo é scroll pra cima, negativo é para baixo 
