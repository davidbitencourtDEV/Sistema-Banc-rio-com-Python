menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor_deposito = float(input("Digite o valor a depositar: "))

        saldo += valor_deposito

        extrato += f"Depósito de R${valor_deposito:.2f}\n"
        print("Deposito realizado com sucesso!")

    elif opcao == "s":

        valor_saque = float(input("Digite o valor a sacar: "))

        if numero_saques < LIMITE_SAQUES:
            if valor_saque <= saldo and valor_saque <= limite:
                saldo -= valor_saque
                numero_saques += 1
                extrato += f"Saque de R${valor_saque:.2f}\n"
                print("Saque realizado com sucesso!")
            else:
                print("Valor de saque inválido.")

        else:
            print("Você atingiu o limite de saques diários. Não é possível sacar mais hoje.")

    elif opcao == "e":
    # Exibir extrato
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("operação invalida, por favor selecione novamente a operação desejada.")

