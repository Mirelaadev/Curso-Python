class Numero:
    def __init__(self, n1, n2, n3):
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3

    def calcular(self):
        maior = self.n1
        menor = self.n1

        if(self.n1 == self.n2 or self.n2 == self.n3 or self.n3 == self.n1):
            return "Os numeros são iguais!"

        if self.n2 > maior:
            maior = self.n2

        if self.n3 > maior:
            maior = self.n3

        if self.n2 < menor:
            menor = self.n2

        if self.n3 < menor:
            menor = self.n3

        print(f"Maior número: {maior} - Menor número: {menor}")

    def exibir_resultado(self):
        return self.calcular()


n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))
n3 = int(input("Digite um número: "))

numero = Numero(n1, n2, n3)
numero.exibir_resultado()
