altura = float(input("Digite a sua altura: "))
sexo = str(input("Digite o seu sexo: ")).upper()

pesoM = 0
pesoF = 0
if sexo == "M":
    pesoM = (72.7*altura) - 58
    print("Seu peso ideal é: {:.2f}".format(pesoM))
else:
    pesoF = (62.1*altura) - 44.7
    print("Seu peso ideal: é {:.2f}".format(pesoF))


peso = float(input("Digite o seu peso: "))
if sexo == "M":
    if peso > pesoM:
        print("Acima do peso")
    if peso < pesoM:
        print("Abaixo do peso")
    if peso == pesoM:
        print("Peso ideal")
elif sexo == "F":
    if peso > pesoF:
        print("Acima do peso")
    if peso < pesoF:
        print("Abaixo do peso")
    if peso == pesoF:
        print("Peso ideal")



