from abc import ABC, abstractmethod
class Conta:
    def __init__(self, saldo:float, numero:int, agencia:str, cliente:'Cliente', historico:'Historico'):
        self._saldo = saldo
        self._numero = numero
        self._agencia = agencia
        self._cliente = cliente
        self._historico = historico

    @property
    def Saldo(self):
        return float(self._saldo)

    @classmethod
    def nova_conta(cls, cliente,numero:int):
        numero = cliente.contas(len)+1
        return cls(cliente, numero)
    
    @Saldo.setter
    def sacar(self, valor:float):
        _saldo = Conta.Saldo
        limite = ContaCorrente.limite
        limite_saques = ContaCorrente.limite_Saques
        valor = Saque.self._valor

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
        _saldo = Conta.Saldo
        valor = Deposito.self._valor

        if valor <= 0:
            return False
        else:
            return True
        
class Transacao(ABC):
    
    @abstractmethod
    def registrar(conta:Conta):
        pass

class Cliente(Transacao): 
    def __init__(self, endereco, *contas:'Conta'):
        self._endereco = endereco
        self._contas = contas

    def realizar_transacao(self, conta:Conta, transacao:Transacao):
        pass

    @classmethod
    def adicionar_conta(self, conta:Conta):
        self._contas.append(conta)

    
    def registrar(cls,conta):
        pass

class ContaCorrente(Conta):
    def __init__(self):
        self._limite = 500
        self._limite_saques = 3

class Historico(Transacao):
    def adicionar_transacao(cls,transacao:Transacao):
        pass

    def registrar(cls,conta:Conta):
        pass

class Saque:
    def __init__(self, valor):
        self._valor = valor

class Deposito:
    def __init__(self, valor):
        self._valor = valor

class PessoaFisica(Cliente):
    def __init__(self, cpf:str, nome:str, data_nascimento:str):
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento


