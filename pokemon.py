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

    def golpear(self, golpe):
        if(golpe == 1):
            print("Golpe: " + self.golpe1)
        elif(golpe == 2):
            print("Golpe: " + self.golpe2)
        elif(golpe == 3):
            print("Golpe: " + self.golpe3)
        elif(golpe == 4):
            print("Golpe: " + self.golpe4)

    def restaurarVida(self):
        self.hp = self.hp + 10
        print("Vida restaurada: " + str(self.hp))

    def defender(self):
        print("Defendido...")

class Lendario(Pokemon):
    def __init__(self, numero, nome, tipo, ataque, defesa, hp, ataqueEsp, defesaEsp, velocidade, genero, golpe1, golpe2, golpe3, golpe4, golpeExtra):
        super().__init__(numero, nome, tipo, ataque, defesa, hp, ataqueEsp, defesaEsp, velocidade, genero, golpe1, golpe2, golpe3, golpe4)
        self.golpeExtra = golpeExtra

    def golpearDuplo(self, golpe):
        if(golpe == 1):
            print("Golpe Duplo!: " + self.golpe1 + " e " + self.golpeExtra)
        elif(golpe == 2):
            print("Golpe Duplo!: " + self.golpe2 + " e " + self.golpeExtra)
        elif(golpe == 3):
            print("Golpe Duplo!: " + self.golpe3 + " e " + self.golpeExtra)
        elif(golpe == 4):
            print("Golpe Duplo!: " + self.golpe4 + " e " + self.golpeExtra)

    def restaurarVida(self):
        self.hp = self.hp + 100
        print("Vida restaurada: " + str(self.hp))

bulbasauro = Pokemon(1, "Bulbasauro", "Grama", 49, 49, 45, 65, 65, 45, "Macho", "Chicote de Cipó", "Lâmina de Folha", "Lâmina de Grama", "Lâmina de Cipó")
giratina = Lendario(2, "Giratina", "Fantasma", 150, 100, 150, 100, 150, 90, "Macho", "Lâmina de Fantasma", "Assustar", "Ataque rápido", "Morte Súbita", "Martelo do Caos")



