# Definição das funções em arquivo 2

# a)
def f_a(caracter):
    texto = ""
    for i in range(6):
        texto = texto + caracter+caracter+caracter+caracter+caracter+caracter + "\n"
    return texto
# fim da função


# b)
def f_b(caracter):
    texto = ""
    for i in range(1, 7):
        texto = texto + caracter * i + "\n"
    return texto
# fim da função


# c)
def f_c(caracter):
    texto = ""
    vazio = " "
    cont = 5
    for i in range(1, 7):
        texto = texto + vazio * cont + caracter * i + "\n"
        cont = cont - 1
    return texto
# fim da função


# d)
def f_d(caracter):
    # Saída de dados
    #print("d)\n")
    num = 3
    j = 3
    for i in range(1, 8, 2):
        print(' ' * j + i * caracter)
        j = j - 1

    i = 1
    for j in range(5, 0, -2):
        print(i * ' ' + j * caracter)
        i = i + 1

# fim da função


# e)
def f_e(caracter):
    texto = ""
    for i in range(6, 0, -1):
        texto = texto + caracter * i + "\n"
    return texto
# fim da função


# f)
def f_f(caracter):
    texto = ""
    vazio = " "
    cont = 0
    for i in range(6, 0, -1):
        texto = texto + vazio * cont + caracter * i + "\n"
        cont = cont + 1
    return texto
# fim da função
