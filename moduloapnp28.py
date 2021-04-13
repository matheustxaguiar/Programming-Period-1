# moduloapnp26 - arquivo 2

# Função de cálculo se é quadrado perfeito

def f_calc_quadrado(num):
    raiz = (num ** 0.5) % 1
    if raiz == 0:
        return True

# fim da função

# Função de cálculo se é capicua

def f_calc_capicua(num):
    num = str(num)
    invert = num[::-1]
    invert = int(invert)
    num = int(num)
    div = num/invert
    if div == 1:
        return True
# fim da função
