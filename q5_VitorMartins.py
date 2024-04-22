from flask import Flask, request, jsonify
import bcrypt

#Professor, não sabia e nem entendi pelos seus slides como que faz o servidor localmente usando python
#Pesquisei a respeito e é mais ou menos desse jeito, o servidor é rodado mas por algum motivo da error 404 not found
#Ao iniciar o terminal e rodar o servidor, python q5_VitorMartins ele poe o servidor no ar, mas da 404 - error
#Não sei mais o que fazer... Tentei por a porta, mas nada..

app = Flask(__name__)

users = [
    {
        'username': 'admin',
        'password_hash': bcrypt.hashpw('admin_password'.encode('utf-8'), bcrypt.gensalt()).decode('utf-8'),
        'balance': 5000.00
    }
]

user_authenticate = lambda username, password: next((user for user in users if user['username'] == username), None)

generate_receipt = lambda value: f"Recibo R$ {value:.2f}"

register_transaction = lambda: "Transação realizada com sucesso!"

close_transaction = lambda: "Fechando transação..."

process_payment_money = lambda user, value: process_transaction(user, value) if float(user['balance']) >= value else "Saldo insuficiente para realizar a transação."

process_payment_transfer = lambda user, value: process_transaction(user, value) if value >= 0 else "O valor da transferência deve ser positivo."

process_payment_credit = lambda user, value: process_transaction(user, value) if float(user['balance']) >= value else "Saldo insuficiente para realizar a transação."

process_transaction = lambda user, value: (generate_receipt(value), register_transaction(), close_transaction(), float(user['balance']) - value)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = user_authenticate(username, password)
    if not user:
        return jsonify({'message': 'Usuário não encontrado'}), 404

    if bcrypt.checkpw(password.encode('utf-8'), user['password_hash'].encode('utf-8')):
        return jsonify({'message': 'Login bem-sucedido', 'balance': user['balance']}), 200
    else:
        return jsonify({'message': 'Credenciais inválidas'}), 401

if __name__ == '__main__':
    app.run(debug=True, port=5000)