h = float(input("Digite a altura da pirâmide: "))
Bmenor = float(input("Digite o valor da base menor: "))
Bmaior = float(input("Digite o valor da base maior: "))

volume = h/3*(Bmaior**2 + Bmenor**2 + (Bmaior**2 * Bmenor**2)**0.5)

print(f"O volume da pirâmide é de {volume}")