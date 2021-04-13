#C:\Users\mathe\PycharmProjects\exerciciosifes\venv
# -*- coding: utf-8 -*-
#
#  apnp23.py
#
#  Copyright 2021
#  Autor: Matheus Teixeira de Aguiar
#  Matricula: 20202BSI0322
#
#  Este programa:
#  a) Definir uma função em Python 3 que calcule o valor do máximo divisor comum (mdc) entre dois números inteiros
#  positivos. Esta função recebe como parâmetro dois números inteiros positivos e retorna o valor do mdc calculado.
#  Para realizar o cálculo do máximo divisor comum entre dois números utilize o algoritmo de Euclides.
#  b) Faça um programa principal que leia 25 conjuntos com 3 números inteiros positivos. Para cada conjunto de três
#  números lidos, imprima os números lidos na ordem em que foram lidos e o valor do mdc calculado. A saída deste
#  programa deverá ser EXATAMENTE conforme o modelo apresentado nos casos de teste abaixo.
#  c) Invocar o programa principal.

###########################
#Código fonte em Python 3
###########################
#Declaração de variáveis

# Programa principal - arquivo 2

# função com o programa principal

import moduloapnp23

def main():
    #Declaração de Variáveis
    n = int()

    #Processamento
    for i in range(0, 25):
        num1 = int(input())
        num2 = int(input())
        num3 = int(input())
        mdc1 = moduloapnp23.mdc(num1, num2)
        n = moduloapnp23.mdc2(mdc1, num3)
    #Saida de Dados
        print("MDC(%d, %d, %d)=%d" % (num1, num2, num3, n))

if __name__ == "__main__":
    main()
#fim
