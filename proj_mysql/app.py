from conexao import Conexao
from mysql.connector import Error
import re

class App:

    def __init__(self, dados):
        
        self.dados = dados

    def Rodar(self):
        while True:
            print("1. Inserir")
            print("2. Atualizar")
            print("3. Sair")
            opcao = input("Escolha uma opção: ")
            if opcao == '1':
                primeiro_nome = input("Insira o primeiro nome: ")
                ultimo_nome = input("Insira o ultimo nome: ")
                email = input("Insira o email: ")
                senha = input("Insira a senha: ")
                cpf = input("Insira o cpf: ")
                dia = input("Insira o dia de nascimento: ")
                mes = input("Insira o mês de nascimento: ")
                ano = input("Insira o ano de nascimento: ")
                data_nascimento = ano + '-' + mes + '-' + dia
                self.dados.Inserir(primeiro_nome, ultimo_nome, email, senha, cpf, data_nascimento)   
            elif opcao == '2':
                primeiro_nome = input("Insira o primeiro nome: ")
                ultimo_nome = input("Insira o ultimo nome: ")
                email = input("Insira o email: ")
                senha = input("Insira a senha: ")
                cpf = input("Insira o cpf: ")
                data_nascimento = input("Insira a data de nascimento: ")
                self.dados.Atualizar(primeiro_nome, ultimo_nome, email, senha, cpf, data_nascimento)  
            elif opcao == '3':
                break
            else:
                print("Opção inválida.")      
           

        self.dados.Desconectar()

if __name__ == "__main__":
    dados = Conexao('localhost', 'root', '', 'pythonproj')
    app = App(dados)
    app.Rodar()