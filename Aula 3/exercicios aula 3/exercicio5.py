import math
angulo = math.radians(float(input("Digite o valor do angulo em graus: ")))

seno = math.sin(angulo)
cosseno = math.cos(angulo)
tangente = math.tan(angulo)

print(f"Angulo digitado: {angulo}° \n Seno: {math.sin(seno)} \n Cosseno: {math.cos(cosseno)} \n Tangente: {math.tan(tangente)}")