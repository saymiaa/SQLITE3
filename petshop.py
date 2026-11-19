import sqlite3

conexao = sqlite3.connect("academia.db")
cursor = conexao.cursor()

print("Banco Conectado!")

# Cria a tabela de pets
cursor.execute("""
    CREATE TABLE IF NOT EXISTS pets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        especie TEXT,
        tutor TEXT,
        idade INTEGER
    )
    """)

    # Cadastra 5 pets apenas se a tabela estiver vazia
cursor.execute("SELECT COUNT(*) FROM pets")
quantidade = cursor.fetchone()[0]

if quantidade == 0:
        pets = [
            ("Nnardinho", "cachorro", "Gabriel", 3),
            ("Miamiau", "gata", "Mirelle", 2),
            ("Neto", "Águia", "Victoria", 5),
            ("Bielzinho", "coelho", "Kennard", 1),
            ("Davisavis", "gato", "Murillo", 4)
        ]

        cursor.executemany("""
        INSERT INTO pets (nome, especie, tutor, idade)
        VALUES (?, ?, ?, ?)
        """, pets)
        conexao.commit()

    # READ: lista todos os pets
print("\n--- TODOS OS PETS ---")
cursor.execute("SELECT * FROM pets")
for pet in cursor.fetchall():
        print(pet)

    # READ: lista apenas os cachorros
print("\n--- APENAS OS CACHORROS ---")
cursor.execute("SELECT * FROM pets WHERE especie = ?", ("cachorro",))
for pet in cursor.fetchall():
        print(pet)

    # UPDATE: altera o tutor do pet de id 2
cursor.execute("""
    UPDATE pets
    SET tutor = ?
    WHERE id = ?
    """, ("Mirelle", 2))
conexao.commit()

print("\nTutor do pet de id 2 atualizado.")

    # DELETE: exclui o pet de id 5
cursor.execute("DELETE FROM pets WHERE id = ?", (5,))
conexao.commit()

print("Pet de id 5 excluído.")

conexao.close()
