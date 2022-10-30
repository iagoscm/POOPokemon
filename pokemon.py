class Pokemon:
    def __init__(self, numero, nome, tipo, ataque, defesa, hp, ataque_esp, defesa_esp, velocidade, genero,
                 golpe1, golpe2, golpe3, golpe4):
        self.numero = numero
        self.nome = nome
        self.tipo = tipo
        self.ataque = ataque
        self.defesa = defesa
        self.hp = hp
        self.ataque_esp = ataque_esp
        self.defesaEsp = defesa_esp
        self.velocidade = velocidade
        self.genero = genero
        self.golpe1 = golpe1
        self.golpe2 = golpe2
        self.golpe3 = golpe3
        self.golpe4 = golpe4

    def golpear(self, golpe):
        if golpe == 1:
            print("Golpe: " + self.golpe1)
        elif golpe == 2:
            print("Golpe: " + self.golpe2)
        elif golpe == 3:
            print("Golpe: " + self.golpe3)
        elif golpe == 4:
            print("Golpe: " + self.golpe4)

    def restaurar_vida(self):
        self.hp = self.hp + 10
        print("Vida restaurada...\nVida atual: " + str(self.hp))

    def defender(self):
        print("Defendido...")


class Lendario(Pokemon):
    def __init__(self, numero, nome, tipo, ataque, defesa, hp, ataque_esp, defesa_esp, velocidade, genero, golpe1,
                 golpe2, golpe3, golpe4, golpe_extra):
        super().__init__(numero, nome, tipo, ataque, defesa, hp, ataque_esp, defesa_esp, velocidade, genero, golpe1,
                         golpe2, golpe3, golpe4)
        self.golpe_extra = golpe_extra

    def golpear_duplo(self, golpe):
        if golpe == 1:
            print("Golpe Duplo!: " + self.golpe1 + " e " + self.golpe_extra)
        elif golpe == 2:
            print("Golpe Duplo!: " + self.golpe2 + " e " + self.golpe_extra)
        elif golpe == 3:
            print("Golpe Duplo!: " + self.golpe3 + " e " + self.golpe_extra)
        elif golpe == 4:
            print("Golpe Duplo!: " + self.golpe4 + " e " + self.golpe_extra)

    def restaurar_vida(self):
        self.hp = self.hp + 100
        print("Vida restaurada...\nVida atual: " + str(self.hp))


bulbasauro = Pokemon(1, "Bulbasauro", "Grama", 49, 49, 45, 65, 65, 45, "Macho", "Chicote de Cipó", "Lâmina de Folha",
                     "Lâmina de Grama", "Lâmina de Cipó")
giratina = Lendario(2, "Giratina", "Fantasma", 150, 100, 150, 100, 150, 90, "Macho", "Lâmina de Fantasma", "Assustar",
                    "Ataque rápido", "Morte Súbita", "Martelo do Caos")

menu = {'1': "Cadastrar Pokemon", '2': "Listar Pokemons", '3': "Batalhar", '4': "Sair"}

pokemons = [bulbasauro, giratina]


def cadastrar_pokemon():
    while True:
        try:
            numero = int(input("Digite o número do Pokemon: "))
        except Exception as e:
            print(f"Algo aconteceu: {e}")
            break
        nome = input("Digite o nome do Pokemon: ")
        tipo = input("Digite o tipo do Pokemon: ")
        try:
            ataque = int(input("Digite o ataque do Pokemon: "))
        except Exception as e:
            print(f"Algo aconteceu: {e}")
            break
        try:
            defesa = int(input("Digite a defesa do Pokemon: "))
        except Exception as e:
            print(f"Algo aconteceu: {e}")
            break
        try:
            hp = int(input("Digite a vida do Pokemon: "))
        except Exception as e:
            print(f"Algo aconteceu: {e}")
            break
        try:
            ataque_esp = int(input("Digite o ataque especial do Pokemon: "))
        except Exception as e:
            print(f"Algo aconteceu: {e}")
            break
        try:
            defesa_esp = int(input("Digite a defesa especial do Pokemon: "))
        except Exception as e:
            print(f"Algo aconteceu: {e}")
            break
        try:
            velocidade = input("Digite a velocidade do Pokemon: ")
        except Exception as e:
            print(f"Algo aconteceu: {e}")
            break
        genero = input("Digite o gênero do Pokemon (M ou F): ")
        if genero != 'M' or 'F':
            print("Digite M ou F para gênero.")
            break
        golpe1 = input("Digite o primeiro golpe do Pokemon: ")
        golpe2 = input("Digite o segundo golpe do Pokemon: ")
        golpe3 = input("Digite o terceiro golpe do Pokemon: ")
        golpe4 = input("Digite o quarto golpe do Pokemon: ")

        poke = Pokemon(numero, nome, tipo, ataque, defesa, hp, ataque_esp, defesa_esp, velocidade, genero, golpe1,
                       golpe2, golpe3, golpe4)

        return poke


def listar_pokemons():
    for poke in pokemons:
        print("Número: " + str(poke.numero))
        print("Nome: " + poke.nome)
        print("Tipo: " + poke.tipo)
        print("Ataque: " + str(poke.ataque))
        print("Defesa: " + str(poke.defesa))
        print("HP: " + str(poke.hp))
        print("Ataque Especial: " + str(poke.ataque_esp))
        print("Defesa Especial: " + str(poke.defesaEsp))
        print("Velocidade: " + str(poke.velocidade))
        print("Gênero: " + poke.genero)
        print("Golpe 1: " + poke.golpe1)
        print("Golpe 2: " + poke.golpe2)
        print("Golpe 3: " + poke.golpe3)
        print("Golpe 4: " + poke.golpe4)


if __name__ == "__main__":
    while True:
        options = menu.keys()
        for entry in options:
            print(entry + " - " + menu[entry])
        selection = input("Selecione uma opção: ")
        if selection == '1':
            pokemon = cadastrar_pokemon()
            if pokemon == 0:
                print("Não foi possível cadastrar o pokemon.")
            else:
                pokemons.append(pokemon)
        elif selection == '2':
            listar_pokemons()
        elif selection == '3':
            print("Batalhar")
        elif selection == '4':
            break
        else:
            print("Opção inválida!")
