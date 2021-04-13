# Função que calcula o produto
def f_produto(n1, n2, maior, menor):
    soma = int(0)
    if n1 % 2 == 1:
        soma = soma + n2

    while n1 >= 1:
        n1 = n1 // 2
        n2 = n2 * 2
        if n1 % 2 == 1:
            soma = soma + n2

    if soma > maior:
        maior = soma

    if soma < menor:
        menor = soma

    return soma, maior, menor
# fim da função