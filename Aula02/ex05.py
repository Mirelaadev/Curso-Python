class Questionario:

    perguntas = [
        'Telefonou para vítima?',
        'Esteve no local do crime?',
        'Mora perto da vítima?',
        'Devia para a vítima?',
        'Já trabalhou com a vítima?'
    ]
    respostas = []
    respostaSim = 0

    def perguntar(self):
        for i in self.perguntas:
            self.respostas.append(input(i))

    def resposta(self):
        for i in self.respostas:
            if i == 'sim':
                self.respostaSim += 1

        if self.respostaSim == 2:
            print("Você foi classificada como um(a) suspeita!")
        elif self.respostaSim == 3 or self.respostaSim == 4:
            print("Você foi classificada como um(a) cúmplice!")
        elif self.respostaSim == 5:
            print("Você foi classificada como um(a) assassino(a)!")
        else:
            print("Você foi classificada como um(a) inocente!")

questionario = Questionario()
questionario.perguntar()
questionario.resposta()



