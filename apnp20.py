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


nvagas = float()
qtdmasculino = float()
qtdfeminino = float()
percentf = float()
cv = float()
soma = float()
maiorcv = float(0.0)
maiorcurso = int()
somatotal = float()


codcurso = int(input("Codigo do curso: "))

while codcurso != 0:
    nvagas = float(input("numero de vagas: "))
    qtdfeminino = float(input("n feminino: "))
    qtdmasculino = float(input("n masculino: "))

    #n candidatos por vaga
    soma = qtdmasculino + qtdfeminino
    cv = soma/nvagas
    percentf = (qtdfeminino/soma)*100

    if cv > maiorcv:
        maiorcv = cv
        maiorcurso = codcurso

    somatotal += soma*1

    print("Curso=%d CV=%.2f Perc Inscritos Feminino=%.2f%%" % (codcurso, cv, percentf))

    codcurso = int(input("Codigo do curso: "))

print("Maior Candidados/Vagas=%.2f foi no curso=%d" % (maiorcv, maiorcurso))
print("Total de inscritos=%.0f" % (somatotal))
