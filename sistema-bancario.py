QUANTIDADE_LIMITE_SAQUES = 3
numero_de_saques = 0
valor_limite_saque=500
saldo = 0.0
extrato = ""        
MENU = """   
        ======= Sistema Bancário =======
        [D] Depositar
        [S] Sacar
        [E] Extrato
        [Q] Sair
        =================================
        Obrigado por utilizar nosso sistema bancário!
        """
while True:
    opcao = input(MENU).strip().upper()


    if opcao == "D":
        valor = float(input("Informe o valor a ser depositado: R$ "))
        if valor  > 0:
            saldo +=valor
            extrato += f"Depósito:  R$ {valor:.2f} \n"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Valor inválido para depósito. Tente novamente.")
    elif opcao == "S":
        
        valor = float(input("Informe o valor a ser sacado: R$ "))     
        
        excedeu_saldo = valor > saldo

        excedeu_limite = valor > valor_limite_saque

        excedeu_saque = numero_de_saques >= QUANTIDADE_LIMITE_SAQUES
        
        excedeu_limite
        
        if excedeu_saldo:
            print("Operação inválida, você não tem saldo suficiente para realizar este saque.")
        
        elif excedeu_limite:
            print(f"Operação inválida, o valor do saque não pode ser maior que R$ {valor_limite_saque:.2f}.")

        elif excedeu_saque:
            print(f"Operação inválida, você já realizou {QUANTIDADE_LIMITE_SAQUES} saques hoje, limite diário atingido.")          
           
        elif valor > 0 :
            saldo -= valor 
            extrato += f"Saque: R$   {valor:.2f} \n"
            numero_de_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Valor inválido para saque. Tente novamente.")
    elif opcao == "E":
        print("=================== EXTRATO BANCÁRIO ===================")
        print ("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo atual: R$ {saldo:.2f}")
        print("=========================================================")
    elif opcao == "Q":
        print("Obrigado por utilizar nosso sistema bancário!")
        break
    else:
        print("Operação inválida, por favor selecione uma opção válida.")

