# C:\Users\mathe\PycharmProjects\exerciciosifes\venv
# -*- coding: utf-8 -*-
#
#  apnp25.py
#
#  Copyright 2021
#  Autor: Matheus Teixeira de Aguiar
#  Matricula: 20202BSI0322
#
#  Este programa:
#  - Faça uma função que receba um número inteiro maior ou igual a zero na base 10 e retorne um número inteiro maior
#  ou igual a zero que representa, na base 3, o número na base 10 fornecido como entrada para esta função.
#  - Faça uma função que receba um número inteiro maior ou igual a zero na base 3 e retorne um número inteiro maior ou
#  igual a zero que representa, na base 10, o número na base 3 fornecido como  entrada para esta função.
#  - Faça um programa principal que LEIA diversos números inteiros maiores ou igual a zero na base 10, para cada número
#  LIDO imprima seu respectivo valor na base 3. Usando o valor na base 3, obtido do número de entrada, converta este
#  valor para a base 10 e imprima o mesmo. Considere que a entrada de encerra quando um número menor que zero for
#  informado pelo usuário.

###########################
# Código fonte em Python 3
###########################
import moduloapnp25


def main():
    #  Declaração de variáveis
    num = float()

    #  Entrada de dados
    num = float(input())

    while num >= 0:
        #  Processamento
        nb3 = moduloapnp25.f_base10_para_base3(num)
        nb10 = moduloapnp25.f_base3_para_base10(nb3)

        #  Saída de dados
        print("ENTRADA = %.0f BASE3 = %.0f BASE10 = %.0f" % (num, nb3, nb10))

        #  Entrada de dados
        num = float(input())


if __name__ == "__main__":
    main()
# fim
