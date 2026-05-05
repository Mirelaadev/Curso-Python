import math
class LojaDeTintas:
    def __init__(self, area):
        self.area = area
        self.litros = self.calcular_Litros()
        self.latasDeTintas = self.calcular_Latas()
        self.precoTintas = self.calcular_precoTintas()

    def calcular_Litros(self):
            return self.area /3

    def calcular_Latas(self):
            return math.ceil(self.calcular_Litros() / 18)

    def calcular_precoTintas(self):
            return self.calcular_Latas() * 80

    def mostrar_resultado(self):
            print("Quantidade de latas de tintas: ", self.latasDeTintas)
            print("Preço total: ", self.precoTintas)

area = float(input("Digite a área a ser pintada : "))
loja = LojaDeTintas(area)
loja.mostrar_resultado()



