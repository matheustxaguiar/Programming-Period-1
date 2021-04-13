def f_converte_decimal(a):
    #n = float(input())

    cont = 0
    casa = 10
    soma = 0
    quo = 1
    while quo != 0:
        quo = a // casa
        rest = a % casa
        soma = soma + rest * 10**cont
        cont = cont + 1
        casa = casa * 10
    soma = soma // 10
    #print(soma)

    return soma

def f_converte_2a9(a10, b):
    # Processamento
    if a10 != 0:
        nc = ""
        while a10 > 0:
            resto = a10 % b
            nc = str(resto) + nc
            a10 = a10 // b
    else:
        nc = "0"

    return nc

def f_converte_hex(a10):
    # Declaração de Variáveis
    div = a10
    soma = ""

    # Processamento
    while div != 0:
        quo = div // 16
        rest = div % 16
        div = quo
        if rest >= 10:
            if rest == 10:
                rest = "A"
            if rest == 11:
                rest = "B"
            if rest == 12:
                rest = "C"
            if rest == 13:
                rest = "D"
            if rest == 14:
                rest = "E"
            if rest == 15:
                rest = "F"
        soma = soma + str(rest)

    return soma