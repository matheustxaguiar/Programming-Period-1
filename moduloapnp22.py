# modulo22 - arquivo 1

# Função de cálculo da raiz quadrada de N>0
def f_calcula_raiz_quadrada(n):
  x = n/2
  for i in range(1, 20):
    x = ((x**2 + n)/(2*x)) + 0
  raiz = x
  return raiz
#fim da função
