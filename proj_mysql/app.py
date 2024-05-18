from conexao import Conexao
import mysql.connector
from mysql.connector import Error

class App:
    def Rodar():
        while True:
            
            print("""
                  1. Inserir
                  2. Atualizar
                  3. Consulta Específica
                  4. Consulta Geral
                  5. Deletar
                  6. Sair
                  """)
            
            opcao = input("Escolha uma opção: ")
            try:
                if opcao == '1':
                    Conexao.Conectar()
                    primeiro_nome = input("Insira o primeiro nome: ")
                    ultimo_nome = input("Insira o ultimo nome: ")
                    email = input("Insira o email: ")
                    senha = input("Insira a senha: ")
                    cpf = input("Insira o cpf: ")
                    dia = input("Insira o dia de nascimento: ")
                    mes = input("Insira o mês de nascimento: ")
                    ano = input("Insira o ano de nascimento: ")
                    data_nascimento = ano + '-' + mes + '-' + dia
                    Conexao.Inserir(primeiro_nome, ultimo_nome, email, senha, cpf, data_nascimento)
                    Conexao.Desconectar()   
                elif opcao == '2':
                    Conexao.Conectar()
                    primeiro_nome = input("Insira o primeiro nome: ")
                    ultimo_nome = input("Insira o ultimo nome: ")
                    email = input("Insira o email: ")
                    senha = input("Insira a senha: ")
                    cpf = input("Insira o cpf: ")
                    dia = input("Insira o dia de nascimento: ")
                    mes = input("Insira o mês de nascimento: ")
                    ano = input("Insira o ano de nascimento: ")
                    data_nascimento = ano + '-' + mes + '-' + dia
                    Conexao.Atualizar(primeiro_nome, ultimo_nome, email, senha, cpf, data_nascimento)
                    Conexao.Desconectar() 
                elif opcao == '3':
                    Conexao.Conectar()
                    email = input("Insira o email: ")
                    resultado = Conexao.ConsultaPersonalizada(email)
                    for busca in resultado:
                        print(busca)
                    Conexao.Desconectar()
                elif opcao == '4':
                    Conexao.Conectar()
                    resultado = Conexao.ConsultaGeral()
                    for busca in resultado:
                        print(busca)
                    Conexao.Desconectar()
                elif opcao == '5':
                    Conexao.Conectar()
                    email = input("Insira o email: ")
                    Conexao.Deletar(email)
                    Conexao.Desconectar()
                elif opcao == '6':
                    break
                else:
                    print("Opção inválida.")      
            except Error as e:
                print(f"Erro: {e}")
                Conexao.Desconectar()
if __name__ == "__main__":
    App.Rodar()