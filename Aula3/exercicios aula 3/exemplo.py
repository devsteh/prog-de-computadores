import math
a = float(input("Digite o angulo em graus: "))
sombra = float(input("Digite o cumprimento da sombra em metros: "))

a = math.radians(a)
h = sombra * math.tan(a)

print(f"A altura do predio é {h:.2f} metros")