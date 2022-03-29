valorCompra = float(input("Digite o valor da sua compra: "))

compraDesconto = valorCompra - 0.20

if valorCompra >= 200.00:
    print("Parabéns, você ganhou desconto de 20% na sua compra!")
    print("Valor da compra: %.2f" %(valorCompra))
    print("Valor da compra com desconto: %.2f" %(compraDesconto))
else:
    print("Valor total da compra: %.2f" %(valorCompra))


    
