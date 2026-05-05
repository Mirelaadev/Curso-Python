class Download:
    def __init__(self, tamArquivo, velInternet):
        self.tamArquivo = tamArquivo
        self.velInternet = velInternet

    def tempAprox(self):
        tempoMin = (self.tamArquivo / (self.velInternet / 8) ) /60
        return tempoMin

    def exibir_resultado(self):
        print("Tempo aproximado de download: {:.2f} minutos".format(self.tempAprox()))

tamanho = float(input("Informe o tamanho do arquivo (MB): "))
velocidade = float(input("Informe a velocidade da internet (Mbps): "))

download = Download(tamanho, velocidade)
download.exibir_resultado()