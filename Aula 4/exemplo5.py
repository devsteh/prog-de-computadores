n1 = float(input("Digite a primeira nota do aluno: "))
n2 = float(input("Digite a segunda nota do aluno: "))

media = (n1 + n2) /2

if media >= 6:
    print(f"Parabéns, você foi aprovado! Sua média é {media}")
else: 
    print(f"Infelizmente você foi reprovado, sua média é {media}")