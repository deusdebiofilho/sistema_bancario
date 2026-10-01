
saldo = 0.0
limite_por_saque = 500.0
extrato = ""
numero_saques = 0
LIMITE_SAQUES_DIARIOS = 3

menu = """
================ MENU ================
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> Escolha uma opção: """


while True:
    opcao = input(menu).strip().lower()

 
    if opcao == "d":
        valor_deposito = float(input("Digite o valor do depósito: R$ "))
        
       
        if valor_deposito > 0:
            saldo += valor_deposito
          
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
            print(f"\n Depósito de R$ {valor_deposito:.2f} realizado com sucesso!")
        else:
            print("\n Operação falhou! O valor informado é inválido (deve ser maior que zero).")


    elif opcao == "s":
        valor_saque = float(input("Digite o valor do saque: R$ "))
    
        excedeu_saldo = valor_saque > saldo
        excedeu_limite = valor_saque > limite_por_saque
        excedeu_saques = numero_saques >= LIMITE_SAQUES_DIARIOS
        valor_invalido = valor_saque <= 0

        if excedeu_saldo:
            print("\n Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print(f"\n Operação falhou! O valor do saque excede o limite de R$ {limite_por_saque:.2f} por operação.")
        elif excedeu_saques:
            print("\n Operação falhou! Número máximo de saques diários atingido.")
        elif valor_invalido:
            print("\n Operação falhou! O valor informado é inválido.")
        else:
        
            saldo -= valor_saque
            extrato += f"Saque: R$ {valor_saque:.2f}\n"
            numero_saques += 1
            print(f"\n Saque de R$ {valor_saque:.2f} realizado com sucesso!")

  
    elif opcao == "e":
        print("\n================ EXTRATO ================")
        
        if not extrato:
            print("Não foram realizadas movimentações.")
        else:
            print(extrato, end="")
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("=========================================")

   
    elif opcao == "q":
        print("\nObrigado por utilizar nosso sistema bancário. Até logo!")
        break

 
    else:
        print("\n Opção inválida, por favor selecione novamente a operação desejada.")
