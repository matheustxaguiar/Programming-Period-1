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
#  - Faça uma função que receba um número inteiro maior ou igual a zero na base 10 e retorne uma string que representa,
#  na base 16, o número na base 10 fornecido como entrada para esta função. As letras de A a F do número hexadecimal
#  deverão estar em maiúsculo.
# - Faça uma função que receba uma string que representa um número maior ou igual a zero na base 16 e retorne um número
#  inteiro maior ou igual a zero que representa, na base 10, o número na base 16 fornecido como  entrada para esta função.#
# - Faça um programa principal que LEIA diversos números inteiros maiores ou igual a zero na base 10, para cada número
# LIDO imprima seu respectivo valor na base 16. Usando o valor na base 16, obtido do número de entrada, converta este
# valor para a base 10 e imprima o mesmo. Considere que a entrada de encerra quando um número menor que zero for
# informado pelo usuário.

###########################
# Código fonte em Python 3
###########################
import moduloapnp29


def main():
    # Entrada de dados
    num = int(input())

    # Processamento
    while num >= 0:
        base16 = moduloapnp29.f_base10_para_base16(num)
        base10 = moduloapnp29.f_base16_para_base10(base16)
        if num == 0:
            base16 = "0"
            base10 = "0"

        # Saída de dados
        print("ENTRADA = %d BASE16 = %s BASE10 = %s" % (num, base16, base10))

        # Entrada de dados
        num = int(input())


# fim da função main

# invocação/chamada do programa principal
if __name__ == "__main__":
    main()
#  fim
