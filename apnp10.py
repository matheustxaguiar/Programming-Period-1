#C:\Users\mathe\PycharmProjects\exerciciosifes
# -*- coding: utf-8 -*-
#
#  Apnp10.py
#
#  Copyright 2021
#  Autor: Matheus Teixeira de Aguiar
#  Matricula: 20202bsi322
#
#  Leia dois números reais quaisquer e armazene-os em variáveis com identificadores num1 e num2.
#  Usando somente operações aritméticas troque os valores entre estas duas variáveis num1 e num2. Exemplo:
#  input=11.2
#  10.5
#  output=Num1 = 10.500 Num2 = 11.200

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

  num1 <- num1+num2;
  num2 <- num1-num2;
  num1 <- num1-num2;

  escreva('Num1 = % Num2 = %' % (num1, num2))
  fimse
fim.
'''

###########################
#Código fonte em Python 3
###########################

#Entrada de dados
num1 = float(input('Primeiro número: '))
num2 = float(input('Segundo núcmero: '))

#Processamento de Dados
num1 = num1+num2
num2 = num1-num2
num1 = num1-num2

#Saída de dados
print('Num1 = %.3f Num2 = %.3f' % (num1, num2))
