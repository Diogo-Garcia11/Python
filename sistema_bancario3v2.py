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
        validacao_cpf = self.validar_cpf(cpf)
        if validacao_cpf is True:
            self._cpf = cpf
        else:
            raise ValueError("CPF inválido")
            return
        self._nome = nome
        self._data_nascimento = data_nascimento
    
    def validar_cpf(self,cpf):
    
        if len(cpf) != 11:
            print("CPF inválido")
            return False
        else:
            D02 = cpf[0:1]
            D03 = cpf[1:2]
            D04 = cpf[2:3] 
            D05 = cpf[3:4] 
            D06 = cpf[4:5] 
            D07 = cpf[5:6] 
            D08 = cpf[6:7] 
            D09 = cpf[7:8] 
            D10 = cpf[8:9]
            D11 = cpf[9:10] 
            C01 = cpf[10:11]
            D02 = int(D02) * 11
            D03 = int(D03) * 10
            D04 = int(D04) * 9
            D05 = int(D05) * 8
            D06 = int(D06) * 7
            D07 = int(D07) * 6
            D08 = int(D08) * 5
            D09 = int(D09) * 4
            D10 = int(D10) * 3
            D11 = int(D11) * 2
            C01 = int(C01)
            soma =  D02 + D03 + D04 + D05 + D06 + D07 + D08 + D09 + D10 + D11
            resto = soma % 11
            ver = 11 - resto
            if C01 == ver:
                print("CPF válido")
                return True
            else:
                print("CPF inválido")
                return False
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
class App:
    def criar_cliente(clientes):
        cpf = input("Insira o CPF: ")
        cliente = App.filtrar_cliente(cpf, clientes)
        if cliente:
            print("Cliente já cadastrado")
            return
        else:
            nome = input("Insira o Nome Completo: ")
            data_nascimento = input("Insira a data de nascimento: ")
            rua = input("Insira a rua: ")
            numero = input("Insira o número: ")
            bairro = input("Insira o bairro: ")
            cidade = input("Insira a cidade: ")
            estado = input("Insira o estado: ")
            endereco = rua + ", " + numero + ", " + bairro + ", " + cidade + "/" + estado
            cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, endereco=endereco)
            clientes.append(cliente)
            print("Cliente cadastrado com sucesso")

    def criar_conta(numero_conta, clientes, contas):
        cpf = input("Insira o CPF: ")
        cliente = App.filtrar_cliente(cpf, clientes)

        if not cliente:
            print("Cliente não encontrado")
            return
        conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
        contas.append(conta)
        cliente.contas.append(conta) 

        print(f"Conta criada com sucesso. Número da conta: {numero_conta}")
    
    def filtrar_cliente(cpf,clientes):
        clientes_filtrados = [cliente for cliente in clientes if cliente._cpf == cpf]
        return clientes_filtrados[0] if clientes_filtrados else None
    
    def recuperar_conta_cliente(cliente):
        if not cliente._contas:
            print("Cliente não possui contas")
            return 
        return cliente._contas[0]
    
    def sacar(clientes):
        cpf = input("Insira o CPF: ")
        cliente = App.filtrar_cliente(cpf, clientes)

        if not cliente:
            print("Cliente não encontrado")
            return
        
        valor = float(input("Insira o valor do saque: "))

        transacao = Saque(valor)

        conta = App.recuperar_conta_cliente(cliente)
        if not conta:
            print("Conta não encontrada")
            return
        
        cliente.realizar_transacao(conta, transacao)
        
    def depositar (clientes):
        cpf = input("Insira o CPF: ")
        cliente = App.filtrar_cliente(cpf, clientes)

        if not cliente:
            print("Cliente não encontrado")
            return
        
        valor = float(input("Insira o valor do depósito: "))

        transacao = Deposito(valor)

        conta = App.recuperar_conta_cliente(cliente)

        cliente.realizar_transacao(conta, transacao)

        if not conta:
            print("Conta não encontrada")
            return
        
    def extrato(clientes):
        cpf = input("Insira o CPF: ")
        cliente = App.filtrar_cliente(cpf, clientes)

        if not cliente:
            print("Cliente não encontrado")
            return

        conta = App.recuperar_conta_cliente(cliente)
        
        print("Extrato")
        transacoes = conta.historico.transacoes

        extrato = ""
        if not transacoes:
            print("Sem transações")
            return
        else:
            for transacao in transacoes:
                extrato += f"\n{transacao['tipo']}:\n\tR$
                {transacao['valor']:.2f}"
        
        print(extrato)
        print(f"Saldo: R$ {conta.saldo:.2f}")  

    def listar_clientes(clientes):
        for cliente in clientes:
            print(cliente)

    def listar_contas(contas):
        for conta in contas:
            print(conta)

if __name__ == "__main__":
    clientes = []
    contas = []
    while True:
        try:
            entrada = int(input("Insira uma operação para realizar: \n1 - Cadastrar Cliente\n2 - Cadastrar conta\n3 - Saque \n4 - Deposito\n5 - Extrato\n6 - Sair\n7 - Listar Clientes\n8 Listar Contas"))
            if entrada == 1: #Cadastrar usuário
                try:
                    App.criar_cliente(clientes)
                except Exception as Error:
                    print(Error)
                    print("Erro ao cadastrar usuário")
                finally: 
                    print("Fim do cadastro de usuário")
            elif entrada == 2: #Cadastrar conta
                try:
                    numero_conta = len(contas) + 1
                    App.criar_conta(numero_conta, clientes, contas)
                except Exception as Error:
                    print(Error)
                    print("Erro ao cadastrar conta")
                finally: 
                    print(f"Fim do cadastro de conta ")
            elif entrada == 3: #Saque  
                try:
                    App.sacar(clientes)
                except Exception as Error:
                    print(Error)
                    print("Erro ao cadastrar conta")
                finally: 
                    print(f"Fim do Saque ")
            elif entrada == 4:  
                try:
                    App.depositar(clientes)
                except Exception as Error:
                    print(Error)
                    print("Erro ao cadastrar conta")
                finally: 
                    print(f"Fim do Deposito ")
            elif entrada == 5: #Extrato         
                try:
                    App.extrato(clientes)
                except Exception as Error:
                    print(Error)
                    print("Erro ao cadastrar conta")
                finally: 
                    print(f"Fim do Extrato ")                                   
            elif entrada == 6: #Sair
                break   
            elif entrada == 7: #Listar Clientes
                try:
                    App.listar_clientes(clientes)
                except Exception as Error:
                    print(Error)
                    print("Erro ao listar clientes")
                finally:
                    print("Fim da listagem de clientes")
            elif entrada == 8: #Listar Contas
                try:
                    App.listar_contas(contas)
                except Exception as Error:
                    print(Error)
                    print("Erro ao listar contas")
                finally:
                    print("Fim da listagem de contas")
        except Exception as Erro:
            print(f"Erro: {Erro}")
    