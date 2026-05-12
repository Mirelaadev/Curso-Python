class Download:
    tamArquivo = 0 #MB
    velInternet = 0 #Mbps
    tempAprox = 0

    def entrada_dados(self):
        self.tamArquivo = float(input("Informe o tamanho do arquivo (MB): "))
        self.velInternet = float(input("Informe a velocidade do internet: "))

    def calcular(self):
        self.velInternet = self.velInternet / 8 #transformando bit em byte
        self.tempAprox = (self.tamArquivo / self.velInternet) / 60

    def exibir_resultado(self):
        print("Tempo aproximado de download em minutos é de ", self.tempAprox)

download = Download()
download.entrada_dados()
download.calcular()
download.exibir_resultado()