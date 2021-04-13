#C:\Users\mathe\PycharmProjects\exerciciosifes
# -*- coding: utf-8 -*-
#
#  Apnp18.py
#
#  Copyright 2021
#  Autor: Matheus Teixeira de Aguiar
#  Matricula: 20202bsi322
#
#   Número primo é aquele que só é divisível por ele mesmo e pela unidade.
#   determine e escreva os números primos compreendidos entre5.000 e 7.000.
###########################
#Algoritmo
###########################
'''

'''

###########################
#Código fonte em Python 3
###########################

#Declaração de variáveis
num1 = int(5000)
num2 = float(7000)
rest2 = float()
rest3 = float()
rest5 = float()
qdiv = int()


#Inicialização de variáveis

#Entrada de dados

#Processamento

while num1 <= num2:
    cont = 0
    for i in range(1, num1+1):
        if (num1 % i) == 0:
            cont = cont + 1
    if cont <= 2:
        #Saída de dados
        print(num1)
    num1 = num1 + 1
