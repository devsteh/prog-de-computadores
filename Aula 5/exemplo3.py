print("Bem vindo ao Hotel chique! Abaixo o preço dos tipos das nossas diárias")
print("Simples: R$255,50")
print("Duplo: R$305,50")
print("Triplo: R$360,50")

tipoDiaria = input("Informe o tipo da diária S - Simples, D - Duplo, T - Triplo: ")
qtdeDias = int(input("Informe a quantidade de dias de hospedagem: "))

if tipoDiaria in "Ss":
    simples = 255.50 * qtdeDias
    print(f"Valor da hospedagem: {simples}")
elif tipoDiaria in"Dd":
    duplo = 305.50 * qtdeDias
    print(f"Valor da hospedagem: {duplo}")
elif tipoDiaria in "Tt":
    triplo = 360.50 *qtdeDias
    print(f"Valor da hospedagem: {triplo}")
else: 
    valor = 0

if valor == 0:
    print("Tipo de diária inválido!")