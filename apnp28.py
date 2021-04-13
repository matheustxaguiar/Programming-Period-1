# C:\Users\mathe\PycharmProjects\exerciciosifes\venv
# -*- coding: utf-8 -*-
#
#  apnp28.py
#
#  Copyright 2021
#  Autor: Matheus Teixeira de Aguiar
#  Matricula: 20202BSI0322
#
#  Este programa:
#  - Faça uma função que receba um número inteiro positivo e retorne um valor boolean verdade se o número for um
#  quadrado perfeito e falso caso contrário. Um número inteiro é considerado um quadrado perfeito se mesmo possuir uma
#  raiz quadrada exata. Ex. 4 é um número quadrado perfeito e 5 não, pois 4 possui 2 como raiz quadrada e 5 possui
#  2.23606 como raiz quadrada. - Faça uma função que receba um número inteiro positivo e retorne um valor boolean
#  verdade se o número for um número capicua e falso caso contrário. Um número é considerado capicua se possuir o mesmo
#  valor quando lido da esquerda para direita e vice-versa  Exs. 101 é capicua, 104 não é capicua, 11 é capicua, 10 não
#  é capicua, 121 é capicua, 1 é capicua, 1230 não é capicua, 1221 é capicua.
#  - Faça um programa principal que GERE números inteiros de 1 a 10001, para cada número gerado imprima próprio número
#  somente uma das frases a seguir, SE O NÚMERO SE ENCAIXAR EM UMA DAS OU NAS DUAS CONDIÇÕES, ou não imprima algo caso
#  contrário

###########################
# Código fonte em Python 3
###########################
import moduloapnp28


def main():
    quadrado = False
    capicua = False
    num = int()
    for num in range(1, 10002, 1):
        quadrado = moduloapnp28.f_calc_quadrado(num)
        capicua = moduloapnp28.f_calc_capicua(num)

        if (capicua and quadrado) == True:
            print("%d EH QUADRADO PERFEITO E CAPICUA" % num)
        else:
            if quadrado == True:
                print("%d EH QUADRADO PERFEITO" % num)
            if capicua == True:
                print("%d EH CAPICUA" % num)


# fim da função main

# invocação/chamada do programa principal
if __name__ == "__main__":

    main()
#  fim
