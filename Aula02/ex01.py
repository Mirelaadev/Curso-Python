import math
class LojaDeTintas:
    area = 0
    litros = 0
    litros_latas = 18
    quant_lata = 0
    precoTintas = 80
    precoTotal = 0

    def calcular(self, area):
        self.area = area
        self.litros = math.ceil(self.area / 3)
        self.quant_lata = math.ceil(self.litros / self.litros_latas)
        self.precoTotal = self.quant_lata * self.precoTintas

    def mostrar_resultado(self):
         print("Quantidade de litros:", self.litros)
         print("Quantidade de latas de tintas:", self.quant_lata)
         print("Preço total:", self.precoTotal)

loja = LojaDeTintas()
loja.calcular(float(input("Digite a área a ser pintada: ")))
loja.mostrar_resultado()



