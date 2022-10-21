class Pokemon:
    def __init__(self, numero, nome, tipo, ataque, defesa, hp, ataqueEsp, defesaEsp, velocidade, genero
    ,golpe1, golpe2, golpe3, golpe4):
        self.numero = numero
        self.nome = nome
        self.tipo = tipo
        self.ataque = ataque
        self.defesa = defesa
        self.hp = hp
        self.ataqueEsp = ataqueEsp
        self.defesaEsp = defesaEsp
        self.velocidade = velocidade
        self.genero = genero
        self.golpe1 = golpe1
        self.golpe2 = golpe2
        self.golpe3 = golpe3
        self.golpe4 = golpe4

    def setNome(self, nome):
        self.nome = nome
    def getNome(self):
        return self.nome
    def setTipo(self, tipo):
        self.tipo = tipo
    def getTipo(self):
        return self.tipo
    def setAtaque(self, ataque):
        self.ataque = ataque
    def getAtaque(self):
        return self.ataque
    def setDefesa(self, defesa):
        self.defesa = defesa
    def getDefesa(self):
        return self.defesa
    def setHp(self, hp):
        self.hp = hp
    def getHp(self):
        return self.hp
    def setAtaqueEsp(self, ataqueEsp):
        self.ataqueEsp = ataqueEsp
    def getAtaqueEsp(self):
        return self.ataqueEsp
    def setDefesaEsp(self, defesaEsp):
        self.defesaEsp = defesaEsp
    def getDefesaEsp(self):
        return self.defesaEsp
    def setVelocidade(self, velocidade):
        self.velocidade = velocidade
    def getVelocidade(self):
        return self.velocidade
    def setGenero(self, genero):
        self.genero = genero
    def getGenero(self):
        return self.genero
    def setNumero(self, numero):
        self.numero = numero
    def getNumero(self):
        return self.numero
    def __setGolpe1(self, golpe1):
        self.golpe1 = golpe1
    def __getGolpe1(self):
        return self.golpe1
    def __setGolpe2(self, golpe2):
        self.golpe2 = golpe2
    def __getGolpe2(self):
        return self.golpe2
    def __setGolpe3(self, golpe3):
        self.golpe3 = golpe3
    def __getGolpe3(self):
        return self.golpe3
    def __setGolpe4(self, golpe4):
        self.golpe4 = golpe4
    def __getGolpe4(self):
        return self.golpe4

    def golpear(self):
        if(self.golpe == 1):
            print("Golpe: " + self.golpe1)
        elif(self.golpe == 2):
            print("Golpe: " + self.golpe2)
        elif(self.golpe == 3):
            print("Golpe: " + self.golpe3)
        elif(self.golpe == 4):
            print("Golpe: " + self.golpe4)

    def restaurarVida(self):
        self.hp = self.hp + 10
        print("Vida restaurada: " + str(self.hp))

    def defender(self):
        print("Defendido...")
