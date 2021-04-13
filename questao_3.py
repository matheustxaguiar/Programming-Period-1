# C:\Users\mathe\PycharmProjects\exerciciosifes\venv
# -*- coding: utf-8 -*-
#
#  questao_3.py
#
#  Copyright 2021
#  Autor: Matheus Teixeira de Aguiar
#  Matricula: 20202BSI0322

###########################
# Código fonte em Python 3
###########################
import moduloquestao_3
i = int(input())
n = int(input())

def main():
    if n >= 0:
        triangulo = moduloquestao_3.f_piramide(i, n)
        print(triangulo)
        i = int(input())
        n = int(input())

# fim da função main

# invocação/chamada do programa principal
if __name__ == "__main__":
    main()
#  fim
