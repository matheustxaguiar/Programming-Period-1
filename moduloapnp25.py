# Definição das funções em arquivo 2

# recebe um número na base 3 e retorna um número na base 10
def f_base3_para_base10(nb3):
    # Declaração de variáveis
    divisor = nb3
    cont = 0
    soma = 0
    quo = int()

    # Processamento
    while divisor != 0:
        quo = divisor // 10
        resto = divisor % 10
        soma = (resto * (3**cont)) + soma
        cont = cont + 1
        divisor = quo
    nb10 = soma

    # Saída de dados
    return nb10
# fim da função


# recebe um número na base 10 e retorna um número na base 3
def f_base10_para_base3(num):
    # Declaração de variáveis
    nb3 = 0
    cont = 1
    divisor = num
    resto = int()

    # Processamento
    while divisor != 0:
        resto = divisor % 3
        divisor = divisor // 3
        nb3 = resto * cont + nb3
        cont = cont * 10

    # Saída de dados
    return nb3
# fim da função
