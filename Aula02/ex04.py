class ArrayInt:

    numeros = []
    tamArray = 0

    def entrada_dados(self):
        tamArray = int(input("Qual o tamanho do array? "))
        for i in range(tamArray):
            self.numeros.append(int(input("Digite um numero: ")))

    def organizar_resultado(self):
        for i in range(len(self.numeros)):
            for j in range(i + 1, len(self.numeros)):
                if self.numeros[i] > self.numeros[j]:
                    temp = self.numeros[i]
                    self.numeros[i] = self.numeros[j]
                    self.numeros[j] = temp

        print(self.numeros)


array = ArrayInt()
array.entrada_dados()
array.organizar_resultado()