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
        print("Vida restaurada...\nVida atual: " + str(self.hp))

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
        print("Vida restaurada...\nVida atual: " + str(self.hp))

bulbasauro = Pokemon(1, "Bulbasauro", "Grama", 49, 49, 45, 65, 65, 45, "Macho", "Chicote de Cipó", "Lâmina de Folha", "Lâmina de Grama", "Lâmina de Cipó")
giratina = Lendario(2, "Giratina", "Fantasma", 150, 100, 150, 100, 150, 90, "Macho", "Lâmina de Fantasma", "Assustar", "Ataque rápido", "Morte Súbita", "Martelo do Caos")

menu = {}
menu['1'] = "Cadastrar Pokemon"
menu['2'] = "Listar Pokemons"
menu['3'] = "Batalhar"
menu['4'] = "Sair"

pokemons = []
pokemons.append(bulbasauro)
pokemons.append(giratina)

def cadastrarPokemon():
    numero = input("Digite o número do Pokemon: ")
    nome = input("Digite o nome do Pokemon: ")
    tipo = input("Digite o tipo do Pokemon: ")
    ataque = input("Digite o ataque do Pokemon: ")
    defesa = input("Digite a defesa do Pokemon: ")
    hp = input("Digite a vida do Pokemon: ")
    ataqueEsp = input("Digite o ataque especial do Pokemon: ")
    defesaEsp = input("Digite a defesa especial do Pokemon: ")
    velocidade = input("Digite a velocidade do Pokemon: ")
    genero = input("Digite o gênero do Pokemon: ")
    golpe1 = input("Digite o primeiro golpe do Pokemon: ")
    golpe2 = input("Digite o segundo golpe do Pokemon: ")
    golpe3 = input("Digite o terceiro golpe do Pokemon: ")
    golpe4 = input("Digite o quarto golpe do Pokemon: ")

    pokemon = Pokemon(numero, nome, tipo, ataque, defesa, hp, ataqueEsp, defesaEsp, velocidade, genero, golpe1, golpe2, golpe3, golpe4)

    return pokemon

def listarPokemons():
    for pokemon in pokemons:
        print("Número: " + str(pokemon.numero))
        print("Nome: " + pokemon.nome)
        print("Tipo: " + pokemon.tipo)
        print("Ataque: " + str(pokemon.ataque))
        print("Defesa: " + str(pokemon.defesa))
        print("HP: " + str(pokemon.hp))
        print("Ataque Especial: " + str(pokemon.ataqueEsp))
        print("Defesa Especial: " + str(pokemon.defesaEsp))
        print("Velocidade: " + str(pokemon.velocidade))
        print("Gênero: " + pokemon.genero)
        print("Golpe 1: " + pokemon.golpe1)
        print("Golpe 2: " + pokemon.golpe2)
        print("Golpe 3: " + pokemon.golpe3)
        print("Golpe 4: " + pokemon.golpe4)

if __name__ == "__main__":
    while True:
        options = menu.keys()
        for entry in options:
            print(entry + " - " + menu[entry])

        selection = input("Selecione uma opção: ")
        if selection == '1':
            pokemon = cadastrarPokemon()
            pokemons.append(pokemon)
        elif selection == '2':
            listarPokemons()
        elif selection == '3':
            print("Batalhar")
        elif selection == '4':
            break
        else:
            print("Opção inválida!")
