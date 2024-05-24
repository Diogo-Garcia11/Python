from abc import ABC, abstractmethod 
from datetime import datetime
class Conta:
    def __init__(self, numero:int,cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @property
    def Saldo(self):
        return float(self._saldo)

    @classmethod
    def nova_conta(cls, cliente,numero:int):
        return cls(cliente, numero)
    
    @Saldo.setter
    def sacar(self, valor:float):
        _saldo = Conta.Saldo
        limite = ContaCorrente._limite
        limite_saques = ContaCorrente._limite_saques
        valor = Cliente.realizar_transacao

        if limite_saques >= 3:
            
            return False
        else:
            if valor > _saldo: 
                return False
            elif valor <= 0:
                return False
            elif valor > limite:
                return False
            else:
                return True

    @Saldo.setter
    def depositar(self, valor:float):
        self._saldo = Conta.Saldo
        valor = Cliente.realizar_transacao

        if valor <= 0:
            return False
        else:
            return True
class ContaCorrente(Conta):
    def __init__(self,  numero,  cliente, limite=500, limite_saques=3):
        super().__init__( numero, cliente, )
        
        self._limite = limite
        self._limite_saques = limite_saques
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
    @classmethod 
    @abstractmethod 
    def registrar(conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor
    
    def registrar(self,conta):
        return Historico.adicionar_transacao(f"Sacou {self._valor}"), conta.self._valor

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor
    
    def registrar(self,conta):

        return Historico.adicionar_transacao(f"Depositou {self._valor}"), conta.self._valor

class Historico:
    
    def adicionar_transacao(transacao):
        transacao.registrar()
