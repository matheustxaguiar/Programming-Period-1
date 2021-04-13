#C:\Users\mathe\PycharmProjects\exerciciosifes\venv
# -*- coding: utf-8 -*-
#
#  apnp22.py
#
#  Copyright 2021
#  Autor: Matheus Teixeira de Aguiar
#  Matricula: 20202BSI0322
#
#  Este programa:
#  a) Definir uma função em Python 3 que calcule o valor da raiz quadrada de um número real positivo N com 20
#  aproximações sucessivas usando o método de Newton descrito no livro do Farrer (página84). Esta função recebe como
#  parâmetro o valor de N. Esta função retorna o valor da raiz quadrada calculada usando o algoritmo de Newton.
# b) Faça um programa principal que leia diversos números reais positivos. Para cada número N lido imprima uma saída
# EXATAMENTE conforme o modelo apresentado nos casos de teste abaixo. A condição de parada da entrada de dados é ler
# um número N menor ou iguail a zero.
# c) Invocar o programa principal.

###########################
#Código fonte em Python 3
###########################
#Declaração de variáveis

# Programa principal - arquivo 2

# função com o programa principal
import moduloapnp22

def main():
    n = float(input(""))
    while n > 0:
        z = moduloapnp22.f_calcula_raiz_quadrada(n)
        print("N=%.8f RAIZ=%.8f" % (n, z))
        n = float(input(""))
#fim da função main

#invocação/chamada do programa principal
if __name__ == "__main__":
  main()
#fim
