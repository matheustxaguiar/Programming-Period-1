#C:\Users\mathe\PycharmProjects\exerciciosifes\venv
# -*- coding: utf-8 -*-
#
#  apnp21.py
#
#  Copyright 2021
#  Autor: Matheus Teixeira de Aguiar
#  Matricula: 20202BSI0322
#
#  Este programa:
#  a) Definir uma função em Python 3 que calcule o valor do fatorial de um número N inteiro maior ou igual a zero.
#  Esta função recebe como parâmetro o valor de N. Esta função retorna o valor do fatorial de N calculado.
#  b) Faça um programa principal que leia diversos números inteiros maiores ou iguais a zero. Para cada número N lido
# imprima uma saída EXATAMENTE conforme o modelo apresentado nos casos de teste abaixo. A condição de parada da entrada
# de dados é ler um número N menor que zero.
#  c) Invocar o programa principal.

###########################
#Código fonte em Python 3
###########################

#Declaração de variáveis
fatorial = int(1)
n = int()


def f_calcula_fatorial(n):
    fatorial = 1
    for i in range(n, 1, -1):
        fatorial = fatorial * i
    return fatorial

def main():
    #Entrada de dados
    n = int(input(""))

    #Processamento
    while n >= 0:
        f = f_calcula_fatorial(n)

        #Saída de dados
        print(f)
        n = int(input(""))

if __name__ == "__main__":
    main()
