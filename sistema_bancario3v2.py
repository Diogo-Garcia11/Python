from abc import ABC, abstractmethod, abstractproperty, abstractclassmethod 
from datetime import datetime
class Conta:
    def __init__(self, numero:int,cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @property
    def saldo(self):
        return float(self._saldo)

    @classmethod
    def nova_conta(cls, cliente,numero:int):
        return cls(cliente, numero)
    

    def sacar(self, valor:float):
        _saldo = self.saldo
        excedeu_saldo = valor > _saldo

        if excedeu_saldo: 
            print("Saldo insuficiente")
            return False
        elif valor <= 0:
            print("Valor inválido")
            return False
        else:
            print("Saque realizado com sucesso")
            _saldo -= valor
            return True            
    
    def depositar(self, valor:float):
        self._saldo = self.saldo
        
        if valor <= 0:
            print("Valor inválido")
            return False
        else:
            _saldo += valor
            return True
class ContaCorrente(Conta):
    def __init__(self,  numero,  cliente, limite=500, limite_saques=3):
        super().__init__( numero, cliente )
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len([transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__])
        excedeu_limite = valor > self._limite
        excedeu_saques = numero_saques >=self.limite_saques
        if excedeu_limite:
            print("Limite de saque atingido")
        elif excedeu_saques:
            print(f"Limite de saques diários: {self._limite_saques} atingido")
        else:
            return super().sacar(valor)
    def __str__(self):
        return f"""\
                Agência:\t {self._agencia}
                C/C:\t {self._numero}
                Titular:\t{self._cliente._nome}
                """                 
class Cliente:
    def __init__(self, endereco:str):
        self._endereco = endereco
        self._contas = []
    
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self._contas.append(conta)
class PessoaFisica(Cliente):
    def __init__(self, cpf:str, nome:str, data_nascimento:datetime, endereco:str):
        super().__init__(endereco)
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento  
class Transacao(ABC):
    @property 
    @abstractmethod
    def valor(self):
        pass
    @classmethod
    @abstractmethod
    def registrar(conta):
        pass
class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor
    
    def registrar(self,conta):
        sucesso_transacao = conta.sacar(self._valor)
        
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)      
class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self,conta):
        sucesso_transacao = conta.sacar(self._valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)         
class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self,transacao):
        self._transacoes.append(
            {
                "tipo" : transacao.__class__.__name__,
                "valor" : transacao._valor,
                "data" : datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            }
        )


if __name__ == "__main__":
    clientes = {}
    contas = {}
    while True:
        try:
            entrada = int(input("Insira uma operação para realizar: \n1 - Cadastrar usuário\n2 - Cadastrar conta\n3 - Entrar Em Uma Conta\n4 - Sair\n5 - Listar Usuários\n6 - Listar Contas\n"))
            if entrada == 1:
                try:
                    clientes = PessoaFisica(clientes)
                except Exception as Error:
                    print(Error)
                    print("Erro ao cadastrar usuário")
                finally: 
                    print("Fim do cadastro de usuário")
            elif entrada == 2:
                try:
                    pass
                except Exception as Error:
                    print(Error)
                    print("Erro ao cadastrar conta")
                finally: 
                    print(f"Fim do cadastro de conta ")
            elif entrada == 3:
                num_conta = input("Insira o Numero da Conta: ")
                nome_completo = input("Insira o Nome Completo: ")
                if 1 == 1:
                    print("Logado com sucesso")
                    while True:
                        try:
                            opcao = int(input("Insira uma operação para realizar: \n1 - Saque\n2 - Depósito\n3 - Extrato\n4 - Sair\n"))
                            if opcao == 1: #Saque
                                pass
                            elif opcao == 2: #Depósito
                                pass
                            elif opcao == 3: #Extrato
                                pass
                            elif opcao == 4: #Sair
                                break
                            else: 
                                print("Opção inválida")
                        except Exception as Erro:
                            print(f"Erro: {Erro}")    
                else:
                    print("Conta não encontrado, tente cadastrar uma conta antes")
            elif entrada == 4:
                break
            elif entrada == 5:
                pass
            elif entrada == 6:
                pass  
        except Exception as Erro:
            print(f"Erro: {Erro}")
    