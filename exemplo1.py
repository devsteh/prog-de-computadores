#Exemplo 1 - Definição de variável
nome = input("Digite seu nome: ")
disciplina = input("Digite a disciplina: ")
nota1 = float(input ("Digite a primeira nota: "))
nota2 = float(input ("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

print ("Olá %s \n Disciplina registrada: %s \n Primeira nota: = %.2f \n Segunda nota: = %.2f"%(nome, disciplina, nota1, nota2))
print ("Sua média é:", media)