salario = float(input("Digite o seu salario: "))

if salario <= 280:
    print("Salário antes do reajuste: R${:.2f}".format(salario*1.20))
    print("Percentual: 20%")
    print("Valor do aumento: ", salario*0.20)
    print("Salário após o aumento: R${:.2f}".format(salario*1.20))

elif salario > 280 and salario <= 700:
    print("Salário antes do reajuste: R${:.2f}".format(salario * 1.15))
    print("Percentual: 15%")
    print("Valor do aumento: ", salario * 0.15)
    print("Salário após o aumento: R${:.2f}".format(salario * 1.15))

elif salario > 700 and salario <= 1500:
    print("Salário antes do reajuste: R${:.2f}".format(salario * 1.10))
    print("Percentual: 10%")
    print("Valor do aumento: ", salario * 0.10)
    print("Salário após o aumento: R${:.2f}".format(salario * 1.10))

else :
    print("Salário antes do reajuste: R${:.2f}".format(salario * 1.05))
    print("Percentual: 5%")
    print("Valor do aumento: ", salario * 0.05)
    print("Salário após o aumento: R${:.2f}".format(salario * 1.05))



