# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)
users = {}

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if 'username' in data and 'password' in data:
        username = data['username']
        password = data['password']
        if username not in users:
            users[username] = password
            return jsonify({'message': 'User registration successful.'})
        else:
            return jsonify({'error': 'Username already exists. Please choose a different username.'}), 400
    else:
        return jsonify({'error': 'Invalid input. Please provide both username and password.'}), 400

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if 'username' in data and 'password' in data:
        username = data['username']
        password = data['password']
        if username in users and users[username] == password:
            return jsonify({'message': 'Access granted. Welcome, {}!'.format(username)})
        else:
            return jsonify({'error': 'Access denied. Invalid username or password.'}), 401
    else:
        return jsonify({'error': 'Invalid input. Please provide both username and password.'}), 400

if __name__ == '__main__':
    app.run()
