l1 = float(input("Digite a altura do primeiro lado do retângulo: "))
l2 = float(input("Digite a altura do segundo lado do retângulo: "))
b1 = float(input("Digite o cumprimento da base inferior do retângulo: "))
b2 = float(input("Digite o cumprimento da base superior do retângulo: "))

perimetro = l1+l2+b1+b2
area = b1 * l1
print (f"Resultado do perímetro do retângulo: {perimetro}")
print (f"Resultado da área do retângulo: {area}")