agua = float(input("Digite o valor total da sua conta de água: "))
luz = float(input("Digite o valor total da sua conta de luz: "))
telefone = float(input("Digite o valor total da sua conta de telefone: "))
salario = float(input("Digite o seu salário: "))

soma = agua + luz + telefone

if (soma > salario) :
    print("O seu salário é suficiente para pagar as contas")
else:
    sobra = salario - soma
    print("Você ainda possuí o saldo de R$ %2.f restantes"%(sobra))
