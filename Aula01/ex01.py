inicio = int(input("Digite o inicio do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))

if inicio < fim:
    for x in range(inicio, fim):
        if x % 2 == 0:
            print(x)
elif inicio > fim:
    for x in range(fim, inicio):
        if x % 2 == 0:
            print(x)
else:
    print("Valores iguais")