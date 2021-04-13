# Definição das funções em arquivo 2

# recebe um número na base 16 e retorna um número na base 10

def f_base16_para_base10(nb16):
    soma = 0
    nb16 = nb16[::-1]
    for i in range(len(nb16)):
        valor = nb16[i]
        if valor == "A":
            valor = 10
        if valor == "B":
            valor = 11
        if valor == "C":
            valor = 12
        if valor == "D":
            valor = 13
        if valor == "E":
            valor = 14
        if valor == "F":
            valor = 15
        valor = int(valor)
        soma = valor * (16**i) + soma
    result = int(soma)
    return result
    #fim da função


# recebe um número na base 10 e retorna um número na base 16
def f_base10_para_base16(nb10):
    dividendo = int(nb10)
    soma = ""
    while dividendo != 0:
        quo = dividendo // 16
        resto = dividendo % 16
        dividendo = quo
        if resto >= 10:
            if resto == 10:
                resto = "A"
            if resto == 11:
                resto = "B"
            if resto == 12:
                resto = "C"
            if resto == 13:
                resto = "D"
            if resto == 14:
                resto = "E"
            if resto == 15:
                resto = "F"
        soma = soma + str(resto)
    result = soma[::-1]
    return result

# fim da função
