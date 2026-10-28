import sqlite3
import random
from pathlib import Path
novatabela = False
novodado = False
novodadoloop = False
consultatodas = False
colunasespecificas = False
usandowhere = False
usandobetween = False
usandolike = False
deletedados = False


CAMINHO_PASTA = Path(__file__).resolve().parent
CAMINHO_BANCO = CAMINHO_PASTA / 'meu_banco.db'
conexao = sqlite3.connect(CAMINHO_BANCO)
cursor = conexao.cursor()
def nomedepessoa():
    pessoa = [
        "Paulo",
        "Sidney",
        "Carla",
        "Edgar",
        "Julio",
        "Evaristo",
        "Luciana" 
    ]
    return random.choice(pessoa)
if novatabela:
    cursor.execute(
        'CREATE TABLE Minha_Tabela ( Data Text, Nome Text, Idade real )'
    )
    conexao.commit()

if novodado:
    cursor.execute(
        'INSERT INTO Minha_Tabela VALUES ("26/10/2026", "Santos", "27")'
    )
    conexao.commit()
if novodadoloop:
    for loop in range(10):
        nomealeatorio = nomedepessoa()
        numero = random.randint(10,20)
        cursor.execute(f'INSERT INTO Minha_Tabela VALUES ("26/10/2026", "{nomealeatorio}", "{numero}")')
        conexao.commit()
if consultatodas:
    consulta = cursor.execute(
        'SELECT * FROM Minha_Tabela'
    ).fetchall()
    for linha in consulta:
        print(linha)
if colunasespecificas:
    consulta = cursor.execute( 'SELECT Nome FROM Minha_Tabela ').fetchall()
    for linha in consulta:
        print(linha)

if usandowhere:
    consulta = cursor.execute( 
        '''
        SELECT * FROM Minha_Tabela
        WHERE Idade <= '25'
        '''
    ).fetchall()
    print(consulta)
if usandobetween:
    consulta = cursor.execute(
        '''
        SELECT * FROM Minha_Tabela
        WHERE Idade BETWEEN 15 AND 20
        '''
    ).fetchall()
    for linha in consulta:
        print(linha)
if usandolike:
    consulta = cursor.execute(
        '''
        SELECT * FROM Minha_Tabela
        WHERE Nome LIKE 's%'
        '''
    ).fetchall()

    for linha in consulta:
        print(linha)
if deletedados:
    cursor.execute(
        '''
        DELETE FROM Minha_Tabela WHERE nome LIKE '%<function%'
        '''
    ).fetchall()
consulta = cursor.execute(
    '''
    SELECT * FROM Minha_Tabela
    '''
).fetchall()
consulta = cursor.execute(
    '''
    DELETE FROM Minha_Tabela
    WHERE Nome LIKE '%<function%' AND '%San'
    '''
)
conexao.commit()
consulta = cursor.execute(
    '''
    SELECT * FROM Minha_Tabela
    '''
).fetchall()


for linha in consulta:
    print(linha)

