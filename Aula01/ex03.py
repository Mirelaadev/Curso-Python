altura = float(input("Digite a sua altura: "))
sexo = str(input("Digite o seu sexo: ")).upper()

if sexo == "M":
    pesoIdeal = (72.7*altura) - 58
else:
    pesoIdeal = (62.1*altura) - 44.7

print("Seu peso ideal: é {:.2f}".format(pesoIdeal))


peso = float(input("Digite o seu peso: "))
if peso > pesoIdeal:
    print("Acima do peso")
else:
    print("Você está com o ideal")