class Populacao:
    popuA = 80000
    popuB = 200000

    taxaCrescA = 1.03
    taxaCrescB = 1.015
    ano = 0

    def calcular(self):
        while self.popuA <= self.popuB:
           self.popuA = self.popuA * self.taxaCrescA
           self.popuB = self.popuB * self.taxaCrescB
           self.ano += 1

    def exibirPopulacao(self):
        print(f'A população A precisa de {self.ano} anos')

pop = Populacao()
pop.calcular()
pop.exibirPopulacao()





