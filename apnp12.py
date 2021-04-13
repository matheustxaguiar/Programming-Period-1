#C:\Users\mathe\PycharmProjects\exerciciosifes
# -*- coding: utf-8 -*-
#
#  Apnp12.py
#
#  Copyright 2021
#  Autor: Matheus Teixeira de Aguiar
#  Matricula: 20202bsi322
#
#   Um material radioativo perde a metade de sua massa inicial a cada 50 segundos. Faça um programa que leia
#   diversas massas iniciais todas maiores que zero, para cada massa inicial lida calcule a quantidade de segundos
#   necessárias para que o valor da massa inicial se torne menor que 0,5. Imprima:
#   - A quantidade de massa inicial, com 3 casas decimais;
#   - A quantidade de massa final, com 3 casas decimais;
#   - A quantidade de segundos total no formato horas:minutos:segundos;
#   Exemplo: MASSA INICIAL=99.999 MASSA FINAL=99.999 TEMPO DECORRIDO=99:99:99

###########################
#Algoritmo
###########################
'''
Algoritmo
inicio
  real: num1; // número real qualquer
  real: num2; // número real qualquer
  real: num1; // número real qualquer
  inteiro: num2; // número inteiro qualquer
  inteiro: num1; // número inteiro qualquer
  inteiro: num2; // número inteiro qualquer
  escreva("Insira o valor de massa: ");
  leia(massa);

    enquanto (massa >= 0 ) faça
      minicial <- massa
      cont <- 0;  //  inicializador do contador
        enquanto (massa >= 0.5) faça  //  teste de condição
          massa <- massa/2;
          cont <- cont + 1;  //  reaiiza a contagem de vezes que foi dividido
        senão
          tempo <- cont * 50;  //  converte as vezes divididas em tempo no formato de 50 segundos para cada vez
          minu <- tempo div 60;  //  converte o tempo em minutos
          segundo <- ((tempo/60) mod 1)*60;  //  converte o tempo de minutos para segundos
          escreva("MASSA INICIAL=%.3f MASSA FINAL=%.3f TEMPO DECORRIDO=0:%.f:%.f" % (minicial, massa, minu, segundo));

        escreva("Insira o valor de massa: ");
        leia(massa);
    senão
    escreva("FIM")
  fimse;
fim.
'''

###########################
#Código fonte em Python 3
###########################
#Declaração de variáveis
massa = 0.0
minicial = 0.0
tempo = 0.0
cont = 0
minu = 0
segundo = 0


#Entrada de Dados
massa = int(input('Insira o valor de massa: '))


while massa >= 0:
    minicial = massa
    cont = 0
    while massa >= 0.5:
        massa = massa/2
        cont = cont + 1  # realiza a contagem de vezes que a massa foi dividida.

    else:

        tempo = cont * 50  # converte as vezes divididas em tempo, uma vez equivalae a 50 segundos.
        minu = tempo // 60  # converte o tempo em minutos
        segundo = ((tempo/60) % 1)*60  # Converte o resto dos minutos em segundos

        print('MASSA INICIAL=%.3f MASSA FINAL=%.3f TEMPO DECORRIDO=0:%.f:%.f' % (minicial, massa, minu, segundo))

    massa = int(input('Insira o valor de massa: '))  # Repete o processo novamente.

else:
    print('FIM')
