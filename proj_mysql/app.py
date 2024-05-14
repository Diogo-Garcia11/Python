from conexao import Conexao
from mysql.connector import Error
import re

class App:
    def Rodar():
        while True:
            
            print("1. Inserir")
            print("2. Atualizar")
            print("3. Sair")
            opcao = input("Escolha uma opção: ")
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
                data_nascimento = input("Insira a data de nascimento: ")
                Conexao.Atualizar(primeiro_nome, ultimo_nome, email, senha, cpf, data_nascimento)
                Conexao.Desconectar() 
            elif opcao == '3':
                break
            else:
                print("Opção inválida.")      

        Conexao.Desconectar()

if __name__ == "__main__":
    App.Rodar()