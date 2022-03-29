#Mesma estrutura do código do exemplo 2 só que com o elif
freq = int(input("Digite a frequência do aluno: "))
media = float(input("Digite a média do aluno: "))

if freq < 75:
    print("Aluno reprovado por falta!")
elif media < 6.0:
        print("O aluno foi reprovado por nota!")
else:
    print("Aluno aprovado!")

