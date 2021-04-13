# C:\Users\mathe\PycharmProjects\exerciciosifes\venv
# -*- coding: utf-8 -*-
#
# questao_2.py
#
# Copyright 2021
# Autor: Matheus Teixeira de Aguiar
# Matrícula: 20202bsi322
#
###########################
# Código fonte em Python 3
###########################
import moduloquestao_2


def main():
    #Inicialização de variáveis
    menor = 3000000000
    maior = -1

    # Entrada de dados
    num1 = int(input())
    num2 = int(input())

    # Processamento
    while num1 > 0 and num2 > 0:
        prod, maior, menor = moduloquestao_2.f_produto(num1, num2, maior, menor)

        # Saída de dados
        print("%dx%d=%d" % (num1, num2, prod))
        num1 = int(input())
        if num1 > 0:
            num2 = int(input())

    # Saída de dados
    print("PRODUTO MAIOR=%d" % maior)
    print("PRODUTO MENOR=%d" % menor)


if __name__ == "__main__":
    main()
#fim