turno = input("Digite o seu turno de trabalho - D para dia ou N para noite: ")
horasTrabalhadas = float(input("Digite suas horas trabalhadas: "))

horaDia = 37.50
horaNoite = 45.00

if turno == "N" or turno == "n":
    salario = horaNoite * horasTrabalhadas
    print(f" Turno de trabalho: Noite \n Horas trabalhadas: {horasTrabalhadas} \n Valor de cada hora trabalhada: {horaNoite} \n Salário a receber: {salario}")
else: #turno == "D" or turno == "d":
    salario = horaDia * horasTrabalhadas
    print(f" Turno de trabalho: Dia \n Horas trabalhadas: {horasTrabalhadas}\n Valor de cada hora trabalhada: {horaDia} \n Salário a receber: {salario}")
