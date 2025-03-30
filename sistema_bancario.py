#deposito, saque e extrato
#3 saques diarios com limite maximo de 500 por saque. Se nao tiver saldo, msg "nao é possivel sacar por falta de saldo". Todo saque deve ser armazenado e exibido na operação de extrato
#listar todos os depositos e saques realizados. No final deve ser exibido o saldo atual. Deve ser em formato R$ xxx, 00

menu = '''

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

'''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "1": #deposito
        valor = float(input("Insira o valor do depósito: "))

        if valor >= 1:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("O valor informado é inválido")
        

    elif opcao == "2": #saque
        saque = float(input("Insira o valor que deseja sacar: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Saldo insuficiente")

        elif excedeu_limite:
            print("Operação falhou! Você não tem saldo suficiente")
        
        elif excedeu_saque:
            print("Operação falhou. Número máximo de saques excedidos")

        elif valor > 0:
            saldo -= saque 
            extrato += f"Saque: R$ {saque:.2f}\n"
            numero_saques +=1

        else:
            print("Operação falhou. Valor informado é inválido")


    elif opcao == "3":
        print("\n~~~~~~~~~~~ Extrato ~~~~~~~~~~")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\n Saldo: R$ {saldo:.2f}")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    elif opcao == "4":
        print("Obrigada por usar nosso sistema! Tenha um ótimo dia!")
        break

    else:
        print("Operação inválida. Por favor, selecione novamente a operação desejada")
