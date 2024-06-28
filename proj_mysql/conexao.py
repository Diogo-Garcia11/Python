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
        try:
            CONEXAO = Conexao.Dados()
            CURSOR = CONEXAO.cursor()
            CURSOR.execute("""
                INSERT INTO tb_usuario (primeiro_nome_usuario, ultimo_nome_usuario, email_usuario, senha_usuario, cpf_usuario, data_nasc_usuario) VALUES (%s, %s, %s, %s, %s, %s)
            """, (primeiro_nome, ultimo_nome, email, senha, cpf, data_nascimento))
            CONEXAO.commit()
            print("Dados Cadastrados com sucesso no banco de dados.")
        except Exception as e:
            print(f"Erro ao inserir: {e}")
            CONEXAO.rollback()
        finally:
            CURSOR.close()
            

    def Atualizar(primeiro_nome, ultimo_nome, email, senha, cpf, data_nascimento):
        try:
            CONEXAO = Conexao.Dados()
            CURSOR = CONEXAO.cursor()
            CURSOR.execute("""
                UPDATE tb_usuario SET primeiro_nome_usuario = %s, ultimo_nome_usuario = %s, email_usuario = %s, senha_usuario = %s, cpf_usuario = %s, data_nasc_usuario = %s WHERE cpf_usuario = %s
            """, (primeiro_nome, ultimo_nome, email, senha, cpf, data_nascimento, cpf))
            CONEXAO.commit()
            print("Dados atualizados com sucesso no banco de dados.")
        except Exception as e:
            print(f"Erro ao atualizar: {e}")
            CONEXAO.rollback()
        finally:
            CURSOR.close()
        
    def ConsultaPersonalizada(email_usuario):
        try:
            CONEXAO = Conexao.Dados()
            CURSOR = CONEXAO.cursor()
            CURSOR.execute("""
                SELECT * FROM tb_usuario WHERE email_usuario = %s
            """, (email_usuario,))
            resultado = CURSOR.fetchall()
            resultado_formatado = [", ".join(map(str, Linha)) for Linha in resultado]
            return resultado_formatado
        except Exception as e:
            print(f"Erro ao consultar: {e}")
        finally:
            CURSOR.close()
    
    def ConsultaGeral():
        try:
            CONEXAO = Conexao.Dados()
            CURSOR = CONEXAO.cursor()
            CURSOR.execute("""
                SELECT * FROM tb_usuario
            """)
            resultado = CURSOR.fetchall()
            CURSOR.close()
            resultado_formatado = [", ".join(map(str, Linha)) for Linha in resultado]
            return resultado_formatado
        except Exception as e:
            print(f"Erro ao consultar: {e}")
        finally:
            CURSOR.close()
        
    def Deletar(email_usuario):
        try:
            CONEXAO = Conexao.Dados()
            CURSOR = CONEXAO.cursor()
            CURSOR.execute("""
                DELETE FROM tb_usuario WHERE email_usuario =%s
            """, (email_usuario,))
            CONEXAO.commit()
            print("Dados Deletados com sucesso no banco de dados.")
        except Exception as e:
            print(f"Erro ao deletar: {e}")
            CONEXAO.rollback()
        finally:
            CURSOR.close()