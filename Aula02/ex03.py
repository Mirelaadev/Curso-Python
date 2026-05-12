class Numero:
    n1 = 0
    n2 = 0
    n3 = 0
    maior = 0
    menor = 0

    def receber_numeros(self, n1, n2, n3):
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3

    def calcular(self):
        self.maior = self.n1
        self.menor = self.n1

        if self.n2 > self.maior:
            self.maior = self.n2

        if self.n3 > self.maior:
            self.maior = self.n3

        if self.n2 < self.menor:
            self.menor = self.n2

        if self.n3 < self.menor:
            self.menor = self.n3

    def exibir_resultado(self):
        print("Maior número: ", self.maior)
        print("Menor número: ", self.menor)

numero = Numero()
numero.receber_numeros(
    float(input("Digite o primeiro número: ")),
    float(input("Digite o segundo número: ")),
    float(input("Digite o terceiro número: "))
)
numero.calcular()
numero.exibir_resultado()
