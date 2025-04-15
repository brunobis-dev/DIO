menu = """

    [1] depositar
    [2] sacar
    [3] extrato
    [4] sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao =="1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito de R$ {valor:.2f} realizado com sucesso.\n"
            print(f"Depósito no valor de {valor:.2f} realizado com sucesso!")

        else:
            print("Valor inválido. Por favor, tente novamente.")

    elif opcao =="2":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saque = numero_saque >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Saldo insuficiente para saque. Por favor, tente novamente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite. Por favor, tente novamente.")

        elif excedeu_saque:
            print("Operação falhou! Número máximo de saques excedido")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque de R$ {valor:.2f} realizado com sucesso.\n"
            numero_saque += 1
            print(f"Saque no valor de {valor:.2f} realizado com sucesso!")

        else:
            print("Operação falhou! O valor informado é inválido")

    elif opcao =="3":

        print("\n==========================EXTRATO==========================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===========================================================")

    elif opcao=="4":
        break

    else:
        print("Opção inválida. Tente novamente.")