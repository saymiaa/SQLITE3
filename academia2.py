
import sqlite3

# CRIOU O BANCO DE DADOS
conexao = sqlite3.connect("academia.db")
cursor = conexao.cursor()

print("Banco Conectado!")

# CRIOU A TABELA
cursor.execute("""
CREATE TABLE IF NOT EXISTS membros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    plano TEXT NOT NULL,
    mensalidade REAL,
    ativo INTEGER
)
""")

# CADASTROU OS MEMBROS
membros = [
    ("Welder", "Premium", 180.0, 1),
    ("Gabriel", "Básico", 90.0, 1),
    ("Kennard", "Família", 250.0, 1),
    ("Davis", "Anual", 130.0, 1),
    ("Neto", "Estudante", 75.0, 0),
    ("Murillo", "Professor", 100.0, 1),
]

cursor.executemany("""
INSERT INTO membros (nome, plano, mensalidade, ativo)
VALUES (?, ?, ?, ?)
""", membros)

conexao.commit()

# LISTOU OS MEMBROS CADASTRADOS
cursor.execute("SELECT * FROM membros")

membros_cadastrados = cursor.fetchall()

for membro in membros_cadastrados:
    print(membro)

# LISTOU OS MEMBROS DO PLANO ANUAL
cursor.execute("SELECT * FROM membros WHERE plano = 'Anual'")

membros_anuais = cursor.fetchall()

for membro in membros_anuais:
    print(membro)

# ATUALIZOU O PLANO DO WELDER
cursor.execute("""
UPDATE membros
SET plano = 'Premium', mensalidade = 180.0
WHERE nome = 'Welder'
""")

conexao.commit()

print("Cadastro e atualização realizados com sucesso!")

# EXCLUIU UM MEMBRO QUE CANCELOU A MATRÍCULA
cursor.execute("""
DELETE FROM membros
WHERE nome = 'Neto'
""")

conexao.commit()

print("Membro excluído com sucesso!")

conexao.close()
