import sqlite3
from pokemon import Pokemon, Lendario

bulbasauro = Pokemon(1, "Bulbasauro", "Grama", 49, 49, 45, 65, 65, 45, "Macho", "Chicote de Cipó", "Lâmina de Folha",
                     "Lâmina de Grama", "Lâmina de Cipó")
bulbasauro.escrever()
giratina = Lendario(2, "Giratina", "Fantasma", 150, 100, 150, 100, 150, 90, "Macho", "Lâmina de Fantasma", "Assustar",
                    "Ataque rápido", "Morte Súbita", "Martelo do Caos")
giratina.escrever()

conexao = sqlite3.connect("pokemon.db")
cursor = conexao.cursor()
cursor.execute("""
        CREATE TABLE pokemon(
            numero text,
            nome text)
        """)
cursor.execute("""
        INSERT INTO pokemon(numero, nome)
            VALUES(?, ?)
            """, (bulbasauro.numero, bulbasauro.nome))
conexao.commit()
cursor.execute("SELECT * FROM pokemon")
resultado = cursor.fetchone()
print(f"Numero: {resultado[0]}\nNome: {resultado[1]}")
cursor.close()
conexao.close()
