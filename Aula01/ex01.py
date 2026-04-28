inicio = int(input("Digite o inicio do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))

for x in range(inicio, fim +1, 2):
    if x % 2 == 0:
        print(x)
    else:
        print(x+1)
