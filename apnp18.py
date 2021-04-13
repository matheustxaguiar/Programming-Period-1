#C:\Users\mathe\PycharmProjects\exerciciosifes
# -*- coding: utf-8 -*-
#
#  Apnp18.py
#
#  Copyright 2021
#  Autor: Matheus Teixeira de Aguiar
#  Matricula: 20202bsi322
#
#   Os bancos atualizam diariamente as contas de seus clientes. Essa atualização envolve a análise dos depósitos e retiradas de cada conta.
#   Numa conta de balanço mínimo, uma taxa de serviço é deduzida se a conta cai abaixo de uma certa quantia especificada.
#   Suponha que uma conta particular comece o dia com um balanço de R$ 60,00. O balanço mínimo exigido é R$ 30,00
#   e se o balanço de fim de dia for menor do que isso, uma taxa é reduzida da conta. A fim de que essa atualização fosse feita
#   utilizando computador, é fornecidoo seguinte conjunto de dados:- a primeira linha contém o valor do balanço mínimo diário, quantidade de transações e taxa deserviço;
#   - as linhas seguintes contém número da conta, valor da transação e código da transação (depósito ou retirada);
#   Escrever um algoritmo que:
#   - calcule o balanço (saldo/débito) da conta ao fim do dia (se o resultado for negativo, isto significa insuficiência de fundos na conta);
#   - escreva, para cada conta, o seu número e o balanço calculado. Se não houver fundos, imprima o número da conta e a mensagem “NÃO HÁ FUNDOS”.

###########################
#Algoritmo
###########################
'''

'''

###########################
#Código fonte em Python 3
###########################
#Declaração de variáveis
nconta = int()
codigo = str()
saldo = float()
balancominimo = float()
qtdtransacao = int()
taxa = float()
valor = float()
debito = float()
credito = float()
total = float()

#Inicialização de variáveis


#Entrada de dados
nconta = int(input('Insira o numero da conta: '))

while nconta != 0:
    saldo = float(input("Saldo: "))
    balancominimo = float(input("Balanço Minimo: "))
    qtdtransacao = int(input('Quantidade de transções: '))
    taxa = float(input("Taxa: "))
    #Processamento
    for i in range(0, qtdtransacao):
        valor = float(input("Valor: "))
        codigo = str(input("Código: "))
        if codigo == "R":
            saldo = saldo - valor

        if codigo == "D":
            saldo = saldo + valor

    if saldo < balancominimo:
        saldo = saldo - taxa

    #Saída de dados
    if saldo < 0:
        print("CONTA=%.d SALDO=%.2f NÃO HÁ FUNDOS" % (nconta, saldo))
    if saldo >= 0:
        print("CONTA=%.d SALDO=%.2f" % (nconta, saldo))

    nconta = int(input('Insira o numero da conta: '))
