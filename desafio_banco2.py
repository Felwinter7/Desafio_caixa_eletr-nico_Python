

def menu_login():
    menu_login = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nu] Criar Usuário
    [nc] Criar conta
    [q] Sair

    => """

    return input(menu_login)


def cadastro_de_usuario(cpf_cadastrado, usuarios):

    nome_usuario = input("=> Escreva o nome do seu usuário: ")
    nome = str(input("=> Nome: "))
    data = (input("=> Data de Nascimento (DD/MM/AA): "))
    cpf = int(input("=> CPF: "))
    endereco = input("=> Endereço (logradouro,nro - bairro - cidade/sigla estado): ")

    if cpf in cpf_cadastrado:
        print("=> Já existe um cadastro realizado com este CPF.")
    else:
        cpf_cadastrado.append(cpf)
        print("=> Cadastro realizado!")
        usuarios.update({nome_usuario:{"nome":nome, "data":data, "cpf":cpf, "endereco":endereco}})
        print(usuarios)


def criar_conta(agencia, numero_conta, usuarios, contas):
    usuario = input("=> Informe seu usuário: ")

    if usuario in usuarios:
        print("=> Conta criada com sucesso! ")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    else:
        print("=> Usuário não encontrado, fluxo de criação de conta encerrado!")


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("=> Depósito realizado com sucesso!")
    else:
        print("=> Operação falhou! O valor informado é inválido.")

    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("=> Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("=> Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("=> Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("=> Saque realizado com sucesso!")

    else:
        print("=> Operação falhou! O valor informado é inválido.")

    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print("------ EXTRATO ------")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("----------------------")


def main():
    AGENCIA = "0001"
    LIMITE_SAQUES = 3

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = {}
    cpf_cadastrado = []
    contas = []
    
  

    while True :

        opcao_login = menu_login()
            
        if opcao_login == "d":
            valor = float(input("Informe o valor que deseja depositar: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao_login == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao_login == "e":
            exibir_extrato(saldo, extrato=extrato)
            
        elif opcao_login == "nu":
            cadastro_de_usuario(cpf_cadastrado, usuarios)

        elif opcao_login == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

main()