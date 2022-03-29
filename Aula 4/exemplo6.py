import math

num = int(input("Digite um número inteiro: "))

raiz = math.sqrt(num)

if num <= 0:
    print("O número digitado é negativo.")
else:
    print("O número digitado é positivo")

print(f"A raiz quadrada de {num} é {raiz}")

#pode ser utilizado o math.sqrt junto da variável padrão sem definir outra