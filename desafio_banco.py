menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato_depositos = []
extrato_saques = []
numero_saques = 0
LIMITES_SAQUES = 3

while True :

    opcao = input(menu)

    if opcao == "d":
        print("Depósito")
        deposito = float(input("Insira o valor que deseja depositar: R$"))

        if deposito > 0:
            saldo = saldo + deposito
            extrato_depositos.append(deposito)
            print(f"Seu saldo atual é: R${saldo:.2f}")
        
        else:
            print("Ocorreu um erro ao realizar o depósito, por favor tente novamente!")
        
    
    elif opcao == "s":
        print("Saque")

        if LIMITES_SAQUES > 0:
            saque = float(input("Informe o valor que deseja sacar: R$"))

            if saque <= saldo:

                if saque <= limite:
                    print(f"Saque realizado com sucesso no valor de R$ + {saque:.2f}")
                    saldo = saldo - saque
                    extrato_saques.append(saque)
                    LIMITES_SAQUES = LIMITES_SAQUES - 1
                    print(f"Seu saldo atual é: R${saldo:.2f}")

                else:
                    print("Valor do saque deve ser inferior ao limite de R$500,00 ")

            else:
                print("Saldo indisponivel!")
        
        else:
            print("O valor de saques diários foi atingido")


    elif opcao == "e":
        print("Extrato")
        print("Seus ultimos depósitos: " + str(extrato_depositos))
        print("Seus ultimos saques: " + str(extrato_saques))
        print("Seu saldo atual é de R$" + str(saldo))


    elif opcao == "q":
        break