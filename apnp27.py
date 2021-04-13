# C:\Users\mathe\PycharmProjects\exerciciosifes\venv
# -*- coding: utf-8 -*-
#
#  apnp27.py
#
#  Copyright 2021
#  Autor: Matheus Teixeira de Aguiar
#  Matricula: 20202BSI0322
#
#  Este programa:
#  - Faça uma função que receba um número inteiro positivo e retorne um valor boolean verdade se o número for primo e
#  falso caso contrário. Um número N inteiro é considerado primo se mesmo for divisível somente por dois números: 1 e
#  por ele mesmo N, e estes dois números são diferentes, por isso, o número 1 não é um número primo.
#  - Faça um programa principal que LEIA diversos números inteiros positivos, para cada número LIDO imprima próprio
#  número somente uma das frases: "EH PRIMO" ou "NAO EH PRIMO". Ao final da leitura dos dados de entrada IMPRIMA a SOMA
#  e o PRODUTO de todos os números lido que forem primos. Considere que a entrada de encerra quando um número menor ou
#  igual a zero for informado pelo usuário.

###########################
# Código fonte em Python 3
###########################
import moduloapnp27


def main():
    # Declaração de variáveis
    soma = int(0)
    prod = int(1)

    # Entrada de dados
    num = int(input())
    while num > 0:
        # Processamento
        primo = moduloapnp27.f_calc_primo(num)
        if primo == 2:
            # Saída de dados
            print("%d EH PRIMO" % num)
            soma = soma + num
            prod = prod * num
        else:
            # Saída de dados
            print("%d NAO EH PRIMO" % num)

        # Entrada de dados
        num = int(input())

    # Saída de dados
    print("SOMA = %d" % soma)
    print("PRODUTO = %d" % prod)

# fim da função main

# invocação/chamada do programa principal


if __name__ == "__main__":

    main()
#  fim
