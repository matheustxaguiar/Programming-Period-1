#C:\Users\mathe\PycharmProjects\exerciciosifes
# -*- coding: utf-8 -*-
#
#  apnp16.py
#
#  Copyright 2021
#  Autor: Matheus Teixeira de Aguiar
#  Matricula: 20202bsi322
#
###########################
#Algoritmo
###########################
'''
Algoritmo.
'''
###########################
#Código fonte em Python 3
###########################
import math

# Declaração de variáveis
tp1 = float()
tp2 = float()
tp3 = float()
ninscricao = int()
tempo1 = float()
tempo2 = float()
tempo3 = float()
d1 = float()
d2 = float()
d3 = float()
etapa1pt = float()
etapa2pt = float()
etapa3pt = float()
pontototal = float()
i = int()
maiorpt = float()
maiorinscricao = int()

# Inicialização de variáveis

tp1 = 0.0
tp2 = 0.0
tp3 = 0.0
ninscricao = 0.0
tempo1 = 0.0
tempo2 = 0.0
tempo3 = 0.0
i = 0
maiorpt = 0.0

# Entrada de dados

tp1 = float(input(""))
tp2 = float(input(""))
tp3 = float(input(""))
ninscricao = int(input(""))

while ninscricao != 9999:
    i = i + 1
    tempo1 = float(input(""))
    tempo2 = float(input(""))
    tempo3 = float(input(""))

    d1 = abs(tp1 - tempo1)
    d2 = abs(tp2 - tempo2)
    d3 = abs(tp3 - tempo3)

    # etapa 1
    if d1 < 3:
        etapa1pt = 100
    if d1 >= 3 and d1 <= 5:
        etapa1pt = 80
    if d1 > 5:
        etapa1pt = 80 - (d1 - 5) / 5
    # etapa2
    if d2 < 3:
        etapa2pt = 100
    if d2 >= 3 and d2 <= 5:
        etapa2pt = 80
    if d2 > 5:
        etapa2pt = 80 - (d2 - 5) / 5
    # etapa3
    if d3 < 3:
        etapa3pt = 100
    if d3 >= 3 and d3 <= 5:
        etapa3pt = 80
    if d3 > 5:
        etapa3pt = 80 - (d3 - 5) / 5

    pontototal = etapa1pt + etapa2pt + etapa3pt

    if pontototal > maiorpt:
        maiorpt = pontototal
        maiorinscricao = ninscricao

    print("EQUIPE=%.d P1=%.2f P2=%.2f P3=%.2f PT=%.2f" % (ninscricao, etapa1pt, etapa2pt, etapa3pt, pontototal))

    ninscricao = int(input(""))
# Saída de dados

if i == 0:
    print("SEM EQUIPES CADASTRADAS")
else:
    print("EQUIPE VENCEDORA=%.d PONTUACAO TOTAL=%.2f" % (maiorinscricao, maiorpt))
