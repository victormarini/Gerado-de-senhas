import pandas as pd
import random
import PySimpleGUI as sg
import os

class passGen:
    def __init__(self):
        sg.theme('LightBrown3')
        layout = [[sg.Text("Site ou aplicação?", size=(15,2)), sg.Input(key = 'site', size=(15,2))],
            [sg.Text('Usuario ou email', size = (15,2)), sg.Input( key = 'usuario', size = (15,2))],
            [sg.Text('Quantidade de caracter'), sg.Combo(values = list(range(31)) ,key = 'total_char', default_value = 1, size = (10,2))],
            [sg.Output(size = (32,5))],
            [sg.Button('gerar senha'), sg.Button('Exit')]]

        self.janela = sg.Window('gerador', layout)
    def iniciar(self):
        while True:
            evento,valores = self.janela.read()
            if evento == sg.WINDOW_CLOSED or evento == 'Exit':
                break
            if evento == "gerar senha":
                nova_senha = self.gerar_senha(valores)
                print(nova_senha)
                self.salvar_senha(nova_senha,valores)
        self.janela.close()
        pass
    def salvar_senha(self,nova_senha,valores):
        with open('senhas.txt','a', newline= '') as arquivo:
            arquivo.write(f"Site:{valores['site']}, Usuario:{valores['usuario']}, Nova senha: {nova_senha}\n")

            print('Arquivo salvo')

        pass

    def gerar_senha (self,valores):

        char_list = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@#"
        chave = random.choices(char_list, k = int(valores['total_char']))
        new_senha = ''.join(chave)

        return new_senha

gen = passGen()
gen.iniciar()
