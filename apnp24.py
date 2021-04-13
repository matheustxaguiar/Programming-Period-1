# C:\Users\mathe\PycharmProjects\exerciciosifes\venv
# -*- coding: utf-8 -*-
#
#  apnp24.py
#
#  Copyright 2021
#  Autor: Matheus Teixeira de Aguiar
#  Matricula: 20202BSI0322
#
#  Este programa:
#  a) Definir uma função em Python 3 que calcule o valor da área do triângulo formado entre uma reta, definida pela
#  equação y = ax + b, e os eixos coordenados (eixo X e eixo Y). Esta função recebe como parâmetros os valores de a e b
#  que definem a equação y = ax + b. Esta função retorna o valor da área calculada do triângulo formado.
#  Atenção: se o valor de a ou o valor de b for igual a zero, não há formação de um triângulo entre a reta y = ax + b e
#  os eixos coordenados (X e Y). Neste caso o valor retornado por esta função para a área calculada deverá ser ZERO.
#  b) Faça um programa principal que leia diversos pares de valores que representam os coeficientes (a e b) da
#  reta y = ax + b. Para cada par (a, b) de valores lidos imprima uma saída EXATAMENTE conforme o modelo apresentado nos
#  casos de teste abaixo. A condição de parada é que os valores fornecidos para a e b sejam ambos iguais a zero.

###########################
# Código fonte em Python 3
###########################
# Declaração de variáveis

# Programa principal - arquivo 1

# função com o programa principal

import moduloapnp24


def main():
    # Declaração de variáveis
    a = float()
    b = float()
    area = float()

    # Entrada de dados
    a = float(input())
    b = float(input())
    while a != 0 or b != 0:
        # Processamento
        area = moduloapnp24.f_calcula_area_triangulo(a, b)

        # Saída de dados
        print("AREA=%.5f A=%.5f B=%.5f" % (area, a, b))

        # Entrada de dados
        a = float(input())
        b = float(input())


if __name__ == "__main__":
    main()
# fim
