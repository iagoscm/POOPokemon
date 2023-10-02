# -*- coding: utf-8 -*-

import sqlite3
from pokemon import Pokemon, Lendario

bulbasauro = Pokemon(1, "Bulbasauro", "Grama", 49, 49, 45, 65, 65, 45, "Macho", "Chicote de Cipó", "Lâmina de Folha",
                     "Lâmina de Grama", "Lâmina de Cipó")
bulbasauro.escrever()
giratina = Lendario(2, "Giratina", "Fantasma", 150, 100, 150, 100, 150, 90, "Macho", "Lâmina de Fantasma", "Assustar",
                    "Ataque rápido", "Morte Súbita", "Martelo do Caos")
giratina.escrever()

pokemons = [bulbasauro, giratina]

conexao = sqlite3.connect("pokemon.db")
cursor = conexao.cursor()
cursor.execute('CREATE TABLE pokemon( numero text, nome text)')

for poke in pokemons:
    cursor.execute("""
            INSERT INTO pokemon(numero, nome)
                VALUES(?, ?)
                """, (poke.numero, poke.nome))
    conexao.commit()
    cursor.execute("SELECT * FROM pokemon")
    print(f'Numero: {poke.numero}\nNome: {poke.nome}')

cursor.close()
conexao.close()

