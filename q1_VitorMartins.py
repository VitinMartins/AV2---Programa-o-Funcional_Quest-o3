transac = lambda: print("Iniciando transação...")

User = [
    {
        'login': 'admin',
        'password': 'admin',
        'balance': 5000.00,
    }
]

user_autentic = lambda login, password: next((usuario for usuario in User if usuario['login'] == login and usuario['password'] == password), None)
receipt = lambda value: print(f"Recibo R$ {value:.2f}")
transaction_made = lambda: print("Transação realizada com sucesso!")
closing = lambda: print("Fechando transação...")

process_payment = lambda usuario, type_transaction, value: (
    process_payment_money(usuario, value) if type_transaction == 'dinheiro' else
    process_payment_transfer(usuario, value) if type_transaction == 'transferencia' else
    process_payment_credit(usuario, value)
)

process_payment_money = lambda usuario, value: (
    process_transaction(usuario, value) if float(usuario['balance']) >= value else
    print("Saldo insuficiente para realizar a transação.")
)

process_payment_transfer = lambda usuario, value: (
    process_transaction(usuario, value) if value >= 0 else
    print("O valor da transferência deve ser positivo.")
)

process_payment_credit = lambda usuario, value: (
    process_transaction(usuario, value) if float(usuario['balance']) >= value else
    print("Saldo insuficiente para realizar a transação.")
)

process_transaction = lambda usuario, value: (
    receipt(value), transaction_made(), closing(), float(usuario['balance']) - value
)

def main():

    transac()

    login = input("Login: ")
    senha = input("Senha: ")

    usuario = user_autentic(login, senha)

    if usuario is None:
        print("Login inválido.")
        return

    end_program = False

    while not end_program:

        tipo_transacao = input("Tipo de transação (dinheiro, transferencia, credito): ")

        valor = float(input("Valor da transação: "))


        resultado_transacao = process_payment(usuario, tipo_transacao, valor)

        if resultado_transacao is not None:
            recibo_valor, transacao_ok_mensagem, fechando_mensagem, novo_saldo = resultado_transacao

            usuario['balance'] = novo_saldo
            print(f"Saldo atualizado: R$ {novo_saldo:.2f}")

        resposta = input("Deseja finalizar as transações? (s/n): ")
        if resposta.lower() == 's':
            end_program = True

    print("\nÚltima transação:")
    print("Tipo:", tipo_transacao)
    print(f"Valor: R$ {valor:.2f}")
    print(f"Saldo atualizado: R$ {usuario['balance']:.2f}")

if __name__ == "__main__":
    main()