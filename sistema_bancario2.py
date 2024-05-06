saldo_conta = 0
limite_saques_diarios = 0
float(saldo_conta)
extrato_conta = []


usuarios ={
        "46764696837":{
            "nome": "xxxxxxxxxxxxxxxxx",
            "cpf": "xxxxxxxxxxx",
            "data_nascimento": "xx/xx/xxxx",
            "endereco": "xxxxxxxx, xxx, xxxxxxx, xxx/xx",
        }
}

conta = {
    "1":{
        "agencia": "0001",
        "conta": "1",
        "usuario": "xxxxxxxxxxxxxxxxxxxx",
    }
}

def validar_cpf(cpf):
    
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
    
def cadastrar_usuario(usuarios):
    nome = input("Insira o Nome Completo: ")
    if nome in [usuario["nome"] for usuario in usuarios.values()]:
        print("Nome já cadastrado")
        return usuarios
    else:
        pass
    cpf = input("Insira o CPF: ")
    validacao_cpf = validar_cpf(cpf)
    if validacao_cpf is False:
        return usuarios
    else:
        pass
    if cpf in usuarios.keys() or cpf in [usuario["cpf"] for usuario in usuarios.values()]:
        print("CPF já cadastrado")
        return usuarios
    else:
        pass
        data_nascimento = input("Insira a data de nascimento: ")
        rua = input("Insira a rua: ")
        numero = input("Insira o número: ")
        bairro = input("Insira o bairro: ")
        cidade = input("Insira a cidade: ")
        estado = input("Insira o estado: ")
        endereco = rua + ", " + numero + ", " + bairro + ", " + cidade + "/" + estado
        usuarios.update({cpf: {"nome": nome, "cpf": cpf, "data_nascimento": data_nascimento, "endereco": endereco}})
        print("Usuário cadastrado com sucesso")
        return usuarios

def cadastrar_conta(conta, usuarios):
    cpf_do_usuario = input("Insira o CPF do usuário: ")
    validacao_cpf = validar_cpf(cpf_do_usuario)
    if validacao_cpf is False:
        return conta, usuarios
    if cpf_do_usuario not in usuarios.keys():
        print("Usuário não encontrado")
        return conta, usuarios
    quem_vai_usar = input("Insira o Nome Completo do usuário: ")
    if quem_vai_usar not in [usuario["nome"] for usuario in usuarios.values()]:
        print("Usuário não encontrado")
        return conta, usuarios
    else:
        usuario_quem = usuarios[cpf_do_usuario]["nome"]

    num_conta = len(conta) + 1

    AGENCIA = "0001"
    conta.update({ num_conta : {"agencia": AGENCIA, "conta": num_conta , "usuarios": usuario_quem}})
    return conta, usuarios

def listar_usuarios():
    for chave, valor in usuarios.items():
        print(chave, valor)

def listar_contas():
    for chave, valor in conta.items():
        print(chave, valor)

def funcao_saque(*,limite, saldo, extrato):
    if limite >= 3:
        print("Limite diário de saques atingido")
        return limite, saldo, extrato
    else:
        saque = float(input("Insira o valor do saque: "))
        if saque > saldo: 
            print("Saldo insuficiente")
            print(f"Saldo: R$  {saldo_conta:.2f}")
            print("Tente depositar antes")
            return limite, saldo, extrato
        elif saque <= 0:
            print("Valor inválido")
            return limite, saldo, extrato
        elif saque > 500:
            print(f"Atingiu o limite de saque: 500, você tentou sacar: {saque:.2f}")
            return limite, saldo, extrato
        else:
            print("Saque realizado com sucesso")
            extrato.append(f"você sacou {saque:.2f}")
            saldo -= saque
            limite += 1
            return limite, saldo, extrato

def funcao_deposito( saldo, extrato):
    deposito = float(input("Insira o valor do depósito: "))
    if deposito <= 0:
        print("Valor inválido")
        return saldo, extrato
    else:
        print("Depósito realizado com sucesso")
        extrato.append(f"voce depositou {deposito:.2f}")
        saldo += deposito   
        return saldo, extrato

def funcao_extrato(saldo,/,*, extrato):
    if extrato == [] or extrato == None:
        print("Nenhuma operação realizada ainda")
    else:
        for i in extrato:
            print(i)
        print(f"Saldo atual: {saldo:.2f}")
    

while True:
    try:
        entrada = int(input("Insira uma operação para realizar: \n1 - Cadastrar usuário\n2 - Cadastrar conta\n3 - Entrar Em Uma Conta\n4 - Sair\n5 - Listar Usuários\n6 - Listar Contas\n"))
        if entrada == 1:
            try:
                usuarios = cadastrar_usuario(usuarios)
            except Exception as Error:
                print(Error)
                print("Erro ao cadastrar usuário")
            finally: 
                print("Fim do cadastro de usuário")
        elif entrada == 2:
            try:
                conta, usuarios = cadastrar_conta(conta, usuarios)
            except Exception as Error:
                print(Error)
                print("Erro ao cadastrar conta")
            finally: 
                print(f"Fim do cadastro de conta ")
        elif entrada == 3:
            num_conta = input("Insira o Numero da Conta: ")
            nome_completo = input("Insira o Nome Completo: ")
            if num_conta in conta.keys() and nome_completo == conta[num_conta]["usuario"]:
                print("Logado com sucesso")
                while True:
                    try:
                        opcao = int(input("Insira uma operação para realizar: \n1 - Saque\n2 - Depósito\n3 - Extrato\n4 - Sair\n"))
                        if opcao == 1: #Saque
                            limite_saques_diarios, saldo_conta, extrato_conta = funcao_saque(limite=limite_saques_diarios, saldo=saldo_conta, extrato=extrato_conta)
                        elif opcao == 2: #Depósito
                            saldo_conta, extrato_conta = funcao_deposito(saldo_conta, extrato_conta)
                        elif opcao == 3: #Extrato
                            funcao_extrato(saldo_conta, extrato=extrato_conta)
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
            listar_usuarios()
        elif entrada == 6:
            listar_contas()  
    except Exception as Erro:
        print(f"Erro: {Erro}")
    
        
        



