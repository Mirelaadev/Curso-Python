print("Tabuada")
numero = int(input("Digite o número da tabuada: "))

if numero > 0 and numero <= 10:
    for x in range(1, 11):
        print(numero, "X", x, "=", (x * numero))
else:
    print("Número invalido")