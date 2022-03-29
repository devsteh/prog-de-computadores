import math

num = float(input("Digite um número real: "))

truncado = math.trunc(num)

print(f"O valor absoluto: {math.fabs(num)} \n A parte inteira: {math.trunc(num)} \n Raiz quadrada: {math.sqrt(num)}\n Fatorial: {math.factorial(truncado)}")
