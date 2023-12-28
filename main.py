from flask import Flask, request, jsonify
import account
app = Flask(__name__)

@app.route('/login', methods=['POST'])
def check_credentials():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if account.login(username,password)==1:

        response = {'status': 'success'}
        
    else:
        response = {'status': 'failure', 'message': 'Invalid credentials'}

    return jsonify(response)

@app.route('/register', methods=['POST'])
def check_register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if account.create_account_user(username,password)==1:

        response = {'status': 'success'}
        
    else:
        response = {'status': 'failure'}

    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
