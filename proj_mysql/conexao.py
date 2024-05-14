# Description: Conexão com o banco de dados MySQL
import mysql.connector
from mysql.connector import Error

class Conexao:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

        self.config = {
            'host': self.host,
            'user': self.user,
            'password': self.password,
            'database': self.database
            }
        self.Conexao = self.Conectar()

    def Conectar(self):
        # """Cria uma conexão com o banco de dados MySQL."""
        try:
            Conexao = mysql.connector.connect(**self.config)
            if Conexao.is_connected():
                print("Conexão bem-sucedida!")
            return Conexao
        except Error as e:
            print(f"Erro ao conectar: {e}")
            return None 
        
    def Desconectar(self):
        # """Fecha a conexão com o banco de dados."""
        if self.Conexao.is_connected():
            self.Conexao.close()
            print("Conexão fechada.")

    def Inserir(self, primeiro_nome, ultimo_nome, email, senha, cpf, data_nascimento):
        # """Insere um novo usuário na tabela."""
        cursor = self.Conexao.cursor()
        cursor.execute("""
            INSERT INTO tb_usuario (primeiro_nome_usuario, ultimo_nome_usuario, email_usuario, senha_usuario, cpf_usuario, data_nasc_usuario) VALUES (%s, %s, %s, %s, %s, %s)
        """, ( primeiro_nome, ultimo_nome, email, senha, cpf, data_nascimento))
        self.Conexao.commit()
        cursor.close()

    def Atualizar(self, primeiro_nome, ultimo_nome, email, senha, cpf, data_nascimento):
        cursor = self.Conexao.cursor()
        cursor.execute("""
            UPDATE tb_usuario SET primeiro_nome_usuario = %s, ultimo_nome_usuario = %s, email_usuario = %s, senha_usuario = %s, cpf_usuario = %s, data_nasc_usuario = %s WHERE cpf_usuario = %s
        """, ( primeiro_nome, ultimo_nome, email, senha, cpf, data_nascimento, cpf))
        self.Conexao.commit()
        cursor.close()