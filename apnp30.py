# C:\Users\mathe\PycharmProjects\exerciciosifes\venv
# -*- coding: utf-8 -*-
#
#  apnp29.py
#
#  Copyright 2021
#  Autor: Matheus Teixeira de Aguiar
#  Matricula: 20202BSI0322
#
#  Este programa:
#  Construa funções 5 em python que produzam e retornem como saída strings contendo os padrões identificados pelas
#  letras de a) a f). Uma função para cada letra (padrão).
#  Em seguida, construa uma aplicação (programa principal) que exibe  vários padrões na tela simplesmente chamando a
#  função responsável de acordo com a entrada que o usuário fornecer: uma letra de a a f para escolha do padrão a ser
#  desenhado e uma letra para informar qual é o caractere a ser impresso pelo padrão. Separe cada padrão impresso por
#  uma linha em branco. Considere que os dados encerram quando o usuário informar uma letra para escolha do padrão com
#  uma letra diferente de a, b, c, d, e ou f.

###########################
# Código fonte em Python 3
###########################
import moduloapnp30

# função main com o programa principal e invocação do programa principal em arquivo 1
def main():
    # Entrada de dados
    padrao = str(input())
    while padrao == "a" or padrao == "b" or padrao == "c" or padrao == "d" or padrao == "e" or padrao == "f":
        # Entrada de dados
        caracter = str(input())

        # Processamento
        if padrao == "a":
            a = moduloapnp30.f_a(caracter)

            # Saída de dados
            #print("a)\n \n%s" % a)
            print(a)
        if padrao == "b":
            b = moduloapnp30.f_b(caracter)

            # Saída de dados
            #print("b)\n \n%s" % b)
            print(b)
        if padrao == "c":
            c = moduloapnp30.f_c(caracter)

            # Saída de dados
            #print("c)\n \n%s" % c)
            print(c)
        if padrao == "d":
            d = moduloapnp30.f_d(caracter)

        if padrao == "e":
            e = moduloapnp30.f_e(caracter)

            # Saída de dados
            #print("e)\n \n%s" % e)
            print(e)
        if padrao == "f":
            f = moduloapnp30.f_f(caracter)
            print(f)

            # Saída de dados
            #print("f)\n \n%s" % f)
        padrao = str(input())


# fim da função main

# invocação/chamada do programa principal
if __name__ == "__main__":
    main()
#  fim
