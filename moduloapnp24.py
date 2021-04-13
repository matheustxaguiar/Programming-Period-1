# moduloapnp24 - arquivo 2

# Função de cálculo da área do triângulo

def f_calcula_area_triangulo(a, b):
    if a == 0 or b == 0:
        area = 0
        return area
    else:
        # distancia em y:
        y = abs(a * 0 + b)

        # distancia em x:
        x = abs((-b / a))
        area = (x * y) / 2
        return area
# fim da função
