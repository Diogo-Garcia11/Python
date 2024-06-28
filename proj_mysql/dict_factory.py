#neste arquivo, diferentemente do app.py, ele retorna os valores do banco de dados em forma de dicionário, e não em forma de tupla.
import mysql.connector
from mysql.connector import Error

def dict_factory(cursor, row):
    return {cursor.description[i][0]: row[i] for i in range(len(row))}

try:
    # Conectar ao banco de dados
    connection = mysql.connector.connect(
        host='localhost',
        database='test_db',
        user='root',
        password='your_password'
    )

    if connection.is_connected():
        cursor = connection.cursor()

        # Criar uma tabela
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            age INT NOT NULL
        )
        ''')

        # Inserir dados
        cursor.execute('''
        INSERT INTO users (name, age) VALUES (%s, %s)
        ''', ('Alice', 30))

        # Confirmar transação
        connection.commit()

        # Selecionar dados
        cursor.execute('SELECT * FROM users')
        rows = cursor.fetchall()

        # Usar a dict_factory para transformar as linhas
        results = [dict_factory(cursor, row) for row in rows]

        for row in results:
            print(row)

except Error as e:
    print(f"Erro: {e}")
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Conexão ao MySQL foi fechada.")
