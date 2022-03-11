#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from platform import *
from requests import get

so = system()
os.path.abspath('python/index.py')
ip = get('https://api.ipify.org').content.decode('utf8')

class printer():
    _colors_ = {
        **dict.fromkeys(("RED", "ERROR", "NO"), "\033[1;31m"),
        **dict.fromkeys(("GREEN", "OK", "YES"), "\033[0;32m"),
        **dict.fromkeys(("YELLOW", "WARN", "MAYBE"), "\033[0;93m"),
        "BLUE": "\033[1;34m",
        "CYAN": "\033[1;36m",
        "RESET": "\033[0;0m",
        "BOLD": "\033[;1m",
        "REVERSE": "\033[;7m"
    }

    def _get_color_(self, key):
            """Gets the corresponding color ANSI code... """
            try:
                return self._colors_[key]
            except:
                return self._colors_["RESET"]

    def print(self, msg , color="RESET"):
            """Main print function..."""

            # Get ANSI color code.
            color = self._get_color_(key=color)

            # Printing...
            print("{}{}{}".format(color, msg, self._colors_["RESET"]))


message = printer()

def MoveFile(path, pathToDestination):
    # In Linux
    os.system(f'mv {path} {pathToDestination}')


def copyFile(file, fileDestination):
    # In Linux/Unix
    os.popen(f'cp {file} {fileDestination} ')
    # In Windows
    os.popen(f'copy {file} {fileDestination}')

def checkOs():
    if so == 'Windows':
        print('Seu Sistema operacional é Windows')
    elif so == 'Linux':
        print("Seu Sistema operacional é Linux :) ")
    else:
        print("Seu sistema operacional não foi indentificado :( ")

def clearOrCls():
    if so == 'Windows' :
        so.system('cls')
    elif so == 'Linux':  
        os.system('clear')

def createFolder(nameFolder):
    folder = os.mkdir(nameFolder)

def menu():
    try:
        option = 0
        while option != 5:
            print('''   choose an option from 1 to 5
                [1] IP   
                [2] Sistema Operacional 
                [3] Limpando a Tela
                [4] Copiar Arquivos 
                [5] Sair ''')
            option = int(input('$:'))
            if option == 1:
                print('My public IP address is: {}'.format(ip))
            elif option == 2:
                checkOs()
            elif option == 3:
                clearOrCls()
            elif option == 4:
                message.print(msg='follow the syntax below', color='YELLOW')
                message.print(msg='Syntax file.text  locale', color='YELLOW')
                a = str(input('>> Digite o arquivo \n>'))
                b = str(input('>> Digite o arquivo \n>'))
                copyFile(a,b)
                print('...')
            elif option == 5:
                print(''' 
                          ⠄⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣀
                          ⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                          ⠄⣾⣿⠿⠛⣉⣁⣤⣤⣤⣤⣬⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠛⠛⠛⠻⠿⠿⣿
                          ⣾⣿⣿⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣤⡈
                          ⣿⣿⣿⣿⠛⢋⠉⠩⠉⢩⣙⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠿⣿⣿⣿
                          ⣿⣿⣿⣿⣿⣿⠿⠶⢶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣶⣏⣁⡁⣐⣆⠈⢻
                          ⣿⣿⣿⣿⣿⣿⣿⣿⡿⢋⣥⣤⡌⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣭⣭⣭⣿⣾⣿
                          ⣿⣿⣿⣿⣿⣿⣿⠿⢀⣿⣿⡿⢁⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                          ⢿⣿⣿⣿⣿⣿⢋⣴⣿⣿⠏⢡⣾⣿⣿⣿⣿⣿⣿⣿⡟⣿⣿⣿⣿⣿⣿⣿⣿⣿
                          ⡈⠙⠛⠛⠻⢃⣼⣿⣿⠏⣐⠻⠿⠿⠿⠿⣿⣿⣿⣿⣿⡜⢿⣿⣿⣿⣿⣿⣿⣿
                          ⣿⣿⣿⡿⢳⣾⣿⣿⠋⣼⣿⣷⣄⠄⠄⠄⠄⠈⠄⢀⣾⣿⣆⠹⣿⣿⡿⠛⠋⠁
                          ⣿⣿⡟⣀⣿⣿⣿⠛⣠⣄⢹⣿⣿⣧⣤⣄⣀⣤⣶⣾⣿⡿⣿⡆⢻⡟⠁⢀⡀⠄
                          ⣿⣿⣷⣿⣿⣿⢣⣾⣿⣿⠄⠉⠄⠄⠈⠉⠉⠃⠉⠉⠛⠃⠉⠈⣾⣷⠾⠟⠁⢠
                          ⠈⠛⠿⣿⣿⣿⣿⣿⣿⠃⣶⣆⢰⣶⣶⣶⣶⠶⠒⢀⣀⣄⣠⣴⡟⠁⠄⠄⣰⣿
                          ⠄⠄⠄⠄⠈⠻⠿⠿⠏⣾⡿⠃⠈⠉⠉⠛⠄⠘⠛⣻⣿⣿⣿⣿⣿⡇⣠⣾⣿⣿                     ''')
                message.print(msg='>>>>>>>>>>> EXIT <<<<<<<<<<<', color='GREEN')
                message.print(msg='By Wesley ( ͡° ͜ʖ ͡°)', color='CYAN')        
            else:
                print('Opção inválida. Tente novamente!')
                clearOrCls()
            print('' * 20)
    except (ValueError, TypeError):
        message.print(msg=' Do not type letters only numbers from 1 to 5', color='RED')
        menu()
    except KeyboardInterrupt:
        message.print(msg=' Unreported Data!', color='RED')
        menu()
menu()