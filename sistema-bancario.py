import textwrap

def menu ():
    menu = """   
        ======= Sistema Bancário =======
        [D] Depositar
        [S] Sacar
        [E] Extrato
        [C] Criar Conta
        [L] Listar Contas
        [NU] Criar Usuário
        [Q] Sair
        =================================
        => Escolha uma Opção:
        """
    return input(textwrap.dedent(menu)).strip().upper()
    

def depositar (saldo,valor,extrato, /):
    if valor  > 0:
        saldo +=valor
        extrato += f"Depósito:  R$ {valor:.2f} \n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Valor inválido para depósito. Tente novamente.")
        
    return saldo, extrato
def sacar (*,saldo,valor,extrato,valor_limite_saque,numero_de_saques,quantidade_limite_saques):
        excedeu_saldo = valor > saldo

        excedeu_limite = valor > valor_limite_saque

        excedeu_saque = numero_de_saques >= quantidade_limite_saques
            
        excedeu_limite
            
        if excedeu_saldo:
            print("Operação inválida, você não tem saldo suficiente para realizar este saque.")
            
        elif excedeu_limite:
            print(f"Operação inválida, o valor do saque não pode ser maior que R$ {valor_limite_saque:.2f}.")

        elif excedeu_saque:
            print(f"Operação inválida, você já realizou {quantidade_limite_saques} saques hoje, limite diário atingido.")          
            
        elif valor > 0 :
            saldo -= valor 
            extrato += f"Saque: R$   {valor:.2f} \n"
            numero_de_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        else:
                print("Valor inválido para saque. Tente novamente.")
                
        return saldo, extrato, numero_de_saques
    
def exibir_extrato (saldo,/,*, extrato):
    print("=================== EXTRATO BANCÁRIO ===================")
    print ("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"Saldo atual: R$ {saldo:.2f}")
    print("=========================================================")

def criar_usuario(usuarios):
    cpf_usuario = input("Informe o CPF do usuário (somente números): ")
    usuario = filtrar_usuario(cpf_usuario, usuarios)
    
    if not filtrar_usuario(cpf_usuario, usuarios):
        nome = input("Informe o nome completo: ")
        endereco = input("Informe o endereço:(Logradouro, Numero, Bairro, Cidade/Estado SIGLA) ")
        data_de_nascimento = input("Informe a data de nascimento (DD/MM/AAAA): ")
        usuarios.append({
            "nome": nome,
            "cpf": cpf_usuario,
            "endereco": endereco,
            "data_nascimento": data_de_nascimento
        })
        
    else:
        print("Usuário já cadastrado.")

    return usuarios
    
def criar_conta(usuarios, numero_conta, agencia):
    cpf_usuario = input("Informe o CPF do usuário (somente números): ")
    usuario = filtrar_usuario(cpf_usuario, usuarios)
    if not usuario:
        print("Usuário não encontrado. Crie um usuário primeiro.")
        return
    senha = input("Informe a senha da conta: ")
    return { "agencia":agencia, "numero_conta":numero_conta, "senha":senha, "usuario":usuario}

   

def filtrar_usuario(cpf,usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario  # retorna o dicionário do usuário encontrado
    return None  # não encontrou ninguém com o CPF
    
def listar_contas(contas):
    if not contas:
        print ("Não existem contas cadastradas")
    for conta in contas:
        usuario = conta["usuario"]
        print (f"Usuario {usuario['nome']}")
        print(f"Agencia:{conta['agencia']} - Conta: {conta['numero_conta']}")
        print ("-"*40)

def main ():
    QUANTIDADE_LIMITE_SAQUES = 3
    numero_de_saques = 0
    valor_limite_saque=500
    saldo = 0.0
    extrato = ""        
    AGENCIA="0001"
    usuarios = []
    contas = []

    while True:
        opcao = menu()


        if opcao == "D":
            valor = float(input("Informe o valor a ser depositado: R$ "))
            saldo, extrato = depositar(saldo,valor,extrato)
           
        elif opcao == "S":
            
            valor = float(input("Informe o valor a ser sacado: R$ "))     
            saldo, extrato,numero_de_saques = sacar (
                saldo=saldo, 
                valor=valor,
                extrato=extrato,    
                valor_limite_saque=valor_limite_saque,
                numero_de_saques=numero_de_saques,
                quantidade_limite_saques=QUANTIDADE_LIMITE_SAQUES
    
            )
            
        
        elif opcao == "E":
            exibir_extrato(saldo, extrato=extrato)
        
        
        elif opcao == "C":
            numero_conta = len(contas) + 1 
            conta = criar_conta(usuarios, numero_conta, AGENCIA)  
            if conta:
                contas.append(conta)
                
            

        elif opcao == "L":
            listar_contas(contas)
            
        elif opcao == "NU":
            
            criar_usuario(usuarios)
        
        elif opcao == "Q":
            print("Obrigado por utilizar nosso sistema bancário!")
            break
        else:
            print("Operação inválida, por favor selecione uma opção válida.")

main()