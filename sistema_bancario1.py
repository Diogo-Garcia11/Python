saldo_conta = 0
limite_saques_diarios = 0
float(saldo_conta)
extrato = []
while True:
    opcao = int(input("Insira uma operação para realizar: \n1 - Saque\n2 - Depósito\n3 - Extrato\n4 - Sair\n"))

    if opcao == 1: #Saque
        if limite_saques_diarios >= 3:
            print("Limite diário de saques atingido")
        else:
            saque = float(input("Insira o valor do saque: "))
            if saque > saldo_conta: 
                print("Saldo insuficiente")
                print("Saldo: R$ ", saldo_conta)
                print("Tente depositar antes")
    
            elif saque <= 0:
                print("Valor inválido")
                
            elif saque > 500:
                print(f"Atingiu o limite de saque: 500, você tentou sacar: {saque}")
            else:
                saldo_conta -= saque
                print("Saque realizado com sucesso")
                extrato.append(f"você sacou: {saque}")
                limite_saques_diarios += 1
            
    elif opcao == 2: #Depósito
        deposito = float(input("Insira o valor do depósito: "))
        if deposito <= 0:
            print("Valor inválido")
        else:
            print("Depósito realizado com sucesso")
            extrato.append(f"voce depositou {deposito}")
            saldo_conta += deposito
            
    elif opcao == 3: #Extrato
        for i in extrato:
            print(i)
        print(f"Saldo atual: {saldo_conta}")
        
    elif opcao == 4: #Sair
        break
    else: 
        print("Opção inválida")
        
