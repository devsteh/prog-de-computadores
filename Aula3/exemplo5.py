import math

num = float(input("Digite um número para cálculo da raiz quadrada: "))
num = math.fabs(num) #retorna o número desconsiderando seu sinal
raiz = math.sqrt(num)
print (f"A raiz de {num} é {raiz:.2f}")