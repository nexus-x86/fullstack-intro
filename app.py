from flask import Flask, request, jsonify, redirect, url_for, send_from_directory, render_template
import os
import json

app = Flask(__name__)
# Needed for flash message functionality
# os.random generates random strings of characters
app.secret_key = os.urandom(12)


# Example JSON entry for users.json
# {
#     "user1": "password1",
#     "user2": "password2"
# } 
def load_users():
    with open('users.json', 'r') as file:
        users = json.load(file)
    return users

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    users = load_users()

    if username in users and users[username] == password:
        return jsonify({'success': True, 'redirect':url_for('chat')})
    else:
        return jsonify({'success': False, 'message':'Incorrect username or password'})

@app.route('/signup', methods=['POST'])
def signup() :
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    users = load_users()
    if username in users:
        return jsonify({'success': False, 'message':'Username already in use'})
    else:
        users[username] = password
        with open('users.json', 'w') as file:
            json.dump(users, file, indent=4)
        return jsonify({'success': True, 'message': 'User registered successfully', 'redirect':"switchLogin"})

@app.route('/switchSignup')
def switchSignup():
    return render_template('signup.html')

@app.route('/switchLogin')
def switchLogin():
    return render_template('login.html')

@app.route('/chat')
def chat():
    return render_template('chat.html')
    #return send_from_directory('templates','chat.html')

@app.route('/')
def index():
    return render_template('login.html')
    #return send_from_directory('templates', 'login.html')

if __name__ == '__main__':
    app.run(debug=True)