# C:\Users\mathe\PycharmProjects\exerciciosifes\venv
# -*- coding: utf-8 -*-
#
# questao_3.py
#
# Copyright 2021
# Autor: Matheus Teixeira de Aguiar
# Matrícula: 20202bsi322
#
###########################
# Código fonte em Python 3
###########################
# Importação dos módulos
import moduloquestao_1


# Função main
def main():
    # Declaração de Variáveis
    saida = ''
    a = 0
    b = 0
    a10 = 0
    inv = ''


    # Entrada de dados
    a = int(input())
    b = int(input())

    # Processamento
    while a >= 0 and b >= 2 and b <= 9:
        a10 = moduloquestao_1.f_converte_decimal(a)
        print(a10)
        comp = moduloquestao_1.f_converte_2a9(a10, b)
        print(comp)
        if(str(a) == comp):
            ahex = moduloquestao_1.f_converte_hex(a10)
            saida = saida + "\n n=" + str(a) + " b=" + str(b) + " n10=" + a10 + " n16=" + ahex
        else:
            inv = "O NUMERO " + str(int(a)) + " ESTAH INVALIDO NA BASE " + str(b)
            saida = saida + "\n" + inv

        # Entrada de dados
        a = int(input())
        if (a >= 0):
            b = int(input())

    # Saída de Dados
    print(saida)


# invocação/chamada do programa principal
if __name__ == "__main__":
    main()
#  fim
