saldo_conta = 0
limite_saques_diarios = 0
float(saldo_conta)
extrato_conta = []


usuarios ={
        "46764696837":{
            "nome": "Diogo Pinheiro Garcia",
            "cpf": "46764696837",
            "data_nascimento": "15/02/2006",
            "endereco": "Rua Lázaro Rossi, 350, Vila Beatriz, São Bernardo do Campo/SP",
        }
}

conta = {
    "1":{
        "agencia": "0001",
        "conta": "1",
        "usuarios": usuarios,
    }
}

def cadastrar_usuario():
    nome = input("Insira o Nome Completo: ")
    cpf = input("Insira o CPF: ")
    if cpf in usuarios.values():
        print("CPF já cadastrado")
    else:
        data_nascimento = input("Insira a data de nascimento: ")
        rua = input("Insira a rua: ")
        numero = input("Insira o número: ")
        bairro = input("Insira o bairro: ")
        cidade = input("Insira a cidade: ")
        estado = input("Insira o estado: ")
        endereco = rua + ", " + numero + ", " + bairro + ", " + cidade + "/" + estado
        usuarios.update({cpf: {"nome": nome, "cpf": cpf, "data_nascimento": data_nascimento, "endereco": endereco}})
        print("Usuário cadastrado com sucesso")

def cadastrar_conta():
    cpf_do_usuario = input("Insira o CPF do usuário: ")
    quem_vai_usar = input("Insira o Nome Completo do usuário: ")
    if quem_vai_usar not in usuarios.values():
        print("Usuário não encontrado")
        return None
    else:
        usuario_quem = usuarios[cpf_do_usuario]["nome"][quem_vai_usar]
    num_conta = 0
    agencia = "001"
    usuarios.update({ num_conta : {"agencia": agencia, "conta": num_conta , "usuarios": usuario_quem}})

def listar_usuarios():
    for chave, valor in usuarios.items():
        print(chave, valor)

def funcao_saque(limite, saldo, extrato):
    if limite >= 3:
        print("Limite diário de saques atingido")
    else:
        saque = float(input("Insira o valor do saque: "))
        if saque > saldo: 
            print("Saldo insuficiente")
            print(f"Saldo: R$  {saldo_conta:.2f}")
            print("Tente depositar antes")
            return None, None, None
        elif saque <= 0:
            print("Valor inválido")
            return None, None, None
        elif saque > 500:
            print(f"Atingiu o limite de saque: 500, você tentou sacar: {saque:.2f}")
            return None, None, None
        else:
            print("Saque realizado com sucesso")
            extrato.append(f"você sacou {saque:.2f}")
            saldo -= saque
            limite += 1
            return saldo, extrato, limite

def funcao_deposito(saldo, extrato):
    deposito = float(input("Insira o valor do depósito: "))
    if deposito <= 0:
        print("Valor inválido")
        return None, None
    else:
        print("Depósito realizado com sucesso")
        extrato.append(f"voce depositou {deposito:.2f}")
        saldo += deposito   
        return saldo, extrato

def funcao_extrato(extrato, saldo):
    if extrato == []:
        print("Nenhuma operação realizada ainda")
    else:
        for i in extrato:
            print(i)
        print(f"Saldo atual: {saldo:.2f}")
    

while True:
    try:
        entrada = int(input("Insira uma operação para realizar: \n1 - Cadastrar usuário\n2 - Cadastrar conta\n3 - Entrar\n4 - Sair\n"))
        if entrada == 1:
            cadastrar_usuario()
            print("Usuário cadastrado com sucesso")
        elif entrada == 2:
            conta = cadastrar_conta()
            print("Conta cadastrada com sucesso, número da conta")
        elif entrada == 3:
            cpf = input("Insira o CPF: ")
            if cpf in usuarios:
                print("Usuário encontrado")
                continue
            else:
                print("Usuário não encontrado")
                entrada = 1
        elif entrada == 4:
            break
        opcao = int(input("Insira uma operação para realizar: \n1 - Saque\n2 - Depósito\n3 - Extrato\n4 - Sair\n"))

        if opcao == 1: #Saque
            limite_saques_diarios, saldo_conta, extrato_conta = funcao_saque(limite=limite_saques_diarios, saldo=saldo_conta, extrato=extrato_conta)
        elif opcao == 2: #Depósito
            saldo_conta, extrato_conta = funcao_deposito(saldo_conta, extrato_conta)
        elif opcao == 3: #Extrato
            funcao_extrato(extrato=extrato_conta, * saldo_conta)
        elif opcao == 4: #Sair
            break
        else: 
            print("Opção inválida")
    except Exception as Erro:
        print(f"Erro: {Erro}")
        
        



