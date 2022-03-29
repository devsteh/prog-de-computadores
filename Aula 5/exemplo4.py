peso = float(input("Informe seu peso: "))
altura = float(input("Informe sua altura: "))

imc = peso/altura**2

if imc < 20:
    print(f"Abaixo do peso. IMC: {imc}")
elif imc >= 20 and imc < 25:
    print(f"Peso normal. IMC: {imc}")
elif imc >= 25 and imc < 30:
    print(f"Sobrepeso. IMC: {imc}")
elif imc >= 40:
    print(f"Obeso. IMC: {imc}")
else:
    print("Obeso Mórbido")