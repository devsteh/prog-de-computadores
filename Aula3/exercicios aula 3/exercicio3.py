anosDigitados = int(input("Digite sua idade: "))
mesesDigitados = int(input("Digite quantos meses você tem: "))
dias = int(input("Digite quantos dias você tem:  "))

ano = 365 * anosDigitados
meses = 30 * mesesDigitados
IdadeDias = (ano + meses + dias)

print(f"Você tem {IdadeDias} dias de idade ")