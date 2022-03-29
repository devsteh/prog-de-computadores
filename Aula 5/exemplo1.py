n1 = float(input("Digite sua primeira nota: "))
n2 = float(input("Digite sua segunda nota: "))

media = (n1+n2)/2

resultado = "Aprovado" if media >= 6 else "Reprovado"

print(f"Você foi {resultado}")