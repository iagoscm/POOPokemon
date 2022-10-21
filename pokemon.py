class Pokemon:
    def __init__(self, numero, nome, tipo, ataque, defesa, hp, ataqueEsp, defesaEsp, velocidade, genero):
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
