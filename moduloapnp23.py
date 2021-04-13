# modulo22 - arquivo 1

# Função de cálculo da raiz quadrada de N>0
def mdc(num1,num2):
    r = num1 % num2
    while (r != 0):
        num1 = num2
        num2 = r
        r = num1 % num2
    return num2

def mdc2(mdc1,num3):
    r = mdc1 % num3
    while (r != 0):
        mdc1 = num3
        num3 = r
        r = mdc1 % num3
    return num3
