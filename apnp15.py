#C:\Users\mathe\PycharmProjects\exerciciosifes
# -*- coding: utf-8 -*-
#
#  Apnp15.py
#
#  Copyright 2021
#  Autor: Matheus Teixeira de Aguiar
#  Matricula: 20202bsi322

############################
#Algoritmo
###########################
'''
Algoritmo.
'''
###########################
#Código fonte em Python 3
###########################

import math

exp = int(0 )
soma = float(0.0)


x = float(input())

funcao = math.exp(x)

while abs(soma-funcao) > 0.0001:
    fat = 1
    #Calculo fatorial
    for i in range(exp, 1, -1):
        fat = fat * 1
    exp = exp + 1
    soma = soma + ((x ** exp) / fat)
    print('teste')

print('%.6f' % (funcao))
print('%.6f' % (soma))

"""
#Saida de dados
print('X=%.6f EXP_FUNCAO(%.6f)=%.6f EXP_SERIE(%.6f)=%.6f' % ())
#print(f'X={x} EXP_FUNCAO({x})={result} EXP_SERIE({x})={e}')
"""

"""
import math

#Declaração de variáveis
e = 0.0
n = 1.0
fat = 1.0
i = 1.0
fatsoma = 2.0

#Entrada de Dados
y = int(input('quantos números?: '))
x = float(input('X: '))
result = math.exp(x)

for s in range(0, y):
#Processamento

    while abs(result-e) >= 0.0001:
        fat = fatsoma * n
        e = ((x ** n) / fat)
        fatsoma = fatsoma + 1
        n = n + 1

        abs(result - e)
        print('teste de looping')
"""