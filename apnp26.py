# C:\Users\mathe\PycharmProjects\exerciciosifes\venv
# -*- coding: utf-8 -*-
#
#  apnp26.py
#
#  Copyright 2021
#  Autor: Matheus Teixeira de Aguiar
#  Matricula: 20202BSI0322
#
#  Este programa:
#  - Faça uma função que receba um número n inteiro positivo e retorne a quantidade de divisores distintos que este
#  número possui. Nesta contagem considere que o valor 1 e o valor n sempre são divisores do número n, por isso todos
#  os números inteiros positivos possuem no mínimo dois divisores que são distintos entre si, exceto o número 1.
#  - Faça um programa principal que leia diversos números inteiros maiores que zero, para cada número lido imprima
#  próprio número e a quantidade de divisores distintos que o número possui. Considere que o programa encerra ao ler
#  um número inteiro menor ou igual a zero.

###########################
# Código fonte em Python 3
###########################
import moduloapnp26


def main():
    # Declaração de variáveis
    div = int()

    # Entrada de dados
    num = int(input())
    while num > 0:
        # Processamento
        div = moduloapnp26.f_calc_divisores(num)
        # Saída de dados
        if div == 1:
            print("%d POSSUI %d DIVISOR" % (num, div))
        else:
            print("%d POSSUI %d DIVISORES" % (num, div))

        # Entrada de dados
        num = int(input())

# fim da função main

# invocação/chamada do programa principal
if __name__ == "__main__":
    main()
#  fim
