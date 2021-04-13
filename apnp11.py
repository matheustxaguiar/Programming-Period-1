#C:\Users\mathe\PycharmProjects\exerciciosifes
# -*- coding: utf-8 -*-
#
#  Apnp10.py
#
#  Copyright 2021
#  Autor: Matheus Teixeira de Aguiar
#  Matricula: 20202bsi322
#
#   leia dois números inteiros quaisquer. Calcule a divisão inteira do primeiro pelo segundo
#   sem utilizar os operadores aritméticos /, // ou % em nenhuma parte de seu código.
#  Se os números forem positivos, imprima:#
#     QUOCIENTE=[#]
# Senão imprima:
#     ENTRADA INVALIDA
# Onde o símbolo [#] representa um valor inteiro sem casas decimais.

###########################
#Algoritmo
###########################
'''
Algoritmo
inicio
  real: num1; // número real qualquer
  real: num2; // número real qualquer
  inteiro = div // número inteiro qualquer
  escreva("Primeiro número: ");
  leia(num1);
  escreva("Segundo número: ");
  leia(num2);

  //Comando condicional composto
  se num1 > 0 e num2 > 0 então
    div <- num1/num2;
    escreva("QUOCIENTE="div);
  senão
    escreva("ENTRADA INVALIDA");
  fimse
fim.
'''

###########################
#Código fonte em Python 3
###########################
#Declaração de variáveis
num1 = float
num2 = float

#Entrada de Dados
print('Primeiro número: ')
num1 = float(input())
print('Segundo número: ')
num2 = float(input())

#Comando condicional composto
if num1 > 0 and num2 > 0:
    div = int((num1/num2))
    print(f'QUOCIENTE={div}')

else:
    print('ENTRADA INVALIDA')
