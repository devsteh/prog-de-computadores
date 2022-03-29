valorPrestacao = float(input("Digite o valor da prestação: "))
multa = int(input("Digite o percentual da multa pelo atraso: "))
qtdeDias = int(input("Digite os dias de atraso da prestação: "))

prestacao = valorPrestacao+(valorPrestacao*(multa/100)*qtdeDias)

print(f"O valor da prestação com juros de atraso é {prestacao}")
