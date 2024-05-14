# Description: Conexão com o banco de dados MySQL
import mysql.connector
from mysql.connector import Error

class Conexao:
    def Dados():
        CONEXAO = mysql.connector.connect(host='localhost',
                                           user='root',
                                           password='', 
                                           database='pythonproj'
                                           )
        return CONEXAO

    def Conectar():
        # """Cria uma conexão com o banco de dados MySQL."""
        try:
            CONEXAO = Conexao.Dados()
            if CONEXAO.is_connected():
                print("Conexão Aberta com sucesso com o banco de dados.")
            return CONEXAO
        except Error as e:
            print(f"Erro ao conectar: {e}")
            return None 
        
    def Desconectar():
        # """Fecha a conexão com o banco de dados."""
        CONEXAO = Conexao.Dados()
        if CONEXAO.is_connected():
            CONEXAO.close()
            print("Conexão fechada com sucesso com o banco de dados.")

    def Inserir(primeiro_nome, ultimo_nome, email, senha, cpf, data_nascimento):
        # """Insere um novo usuário na tabela."""
        CONEXAO = Conexao.Dados()
        CURSOR = CONEXAO.cursor()
        CURSOR.execute("""
            INSERT INTO tb_usuario (primeiro_nome_usuario, ultimo_nome_usuario, email_usuario, senha_usuario, cpf_usuario, data_nasc_usuario) VALUES (%s, %s, %s, %s, %s, %s)
        """, (primeiro_nome, ultimo_nome, email, senha, cpf, data_nascimento))
        CONEXAO.commit()
        CURSOR.close()
        print("Dados Cadastrados com sucesso no banco de dados.")

    def Atualizar(primeiro_nome, ultimo_nome, email, senha, cpf, data_nascimento):
        CONEXAO = Conexao.Dados()
        CURSOR = CONEXAO.cursor()
        CURSOR.execute("""
            UPDATE tb_usuario SET primeiro_nome_usuario = %s, ultimo_nome_usuario = %s, email_usuario = %s, senha_usuario = %s, cpf_usuario = %s, data_nasc_usuario = %s WHERE cpf_usuario = %s
        """, (primeiro_nome, ultimo_nome, email, senha, cpf, data_nascimento, cpf))
        CONEXAO.commit()
        CURSOR.close()
        print("Dados atualizados com sucesso no banco de dados.")

    def Consultar(email_usuario):
        CONEXAO = Conexao.Dados
        CURSOR = CONEXAO.cursor()
        CURSOR.execute("""
            SELECT * FROM tb_usuarios WHERE email_usuario = %s
        """, (email_usuario))
        resultado = CURSOR.fetchall()
        CURSOR.close()
        return resultado
    
    def Deletar(email_usuario)
        CONEXAO.Conexao.Dados
        CURSOR = CONEXAO.cursor()
        CURSOR.executr("""
            DELETE FROM tb_usuarios WHERE email_usuario =%s
        """, (email_usuario))
        CONEXAO.commit()
        CURSOR.close()
        print("Dados Deletados com sucesso no banco de dados.")
    