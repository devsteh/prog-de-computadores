a = int(input("Valor do 1º coeficiente: "))
b = int(input("Valor do 2º coeficiente: "))
c = int(input("Valor do 3º coeficiente: "))

delta = b**2 - 4*a*c
print(f"O valor de delta é: {delta}")

x1 = (-b - delta**0.5) / (2*a)
print(f"O valor do x1 é {x1:.2f}")

x2 = (-b + delta**0.5) / (2*a)
print(f"O valor do x2 é {x2:.2f}")  