# moduloapnp26 - arquivo 2

# Função de cálculo da quantidade de divisores

def f_calc_divisores(num):
    div = 0
    for i in range(num, 0, -1):
        rest = num % i
        if rest == 0:
            div = div + 1
    return div
# fim da função
