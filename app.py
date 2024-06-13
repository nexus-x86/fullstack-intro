from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import json
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

DATA_FILE = 'data/users.json'
MESSAGES_FILE = 'data/messages.json'

def load_users():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_users(users):
    with open(DATA_FILE, 'w') as f:
        json.dump(users, f)

def load_messages():
    if os.path.exists(MESSAGES_FILE):
        with open(MESSAGES_FILE, 'r') as f:
            return json.load(f)
    return []

def save_messages(messages):
    with open(MESSAGES_FILE, 'w') as f:
        json.dump(messages, f)

@app.route('/')
def index():
    if 'username' in session:
        return render_template('index.html', username=session['username'])
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users = load_users()
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('index'))
        return 'Invalid credentials'
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users = load_users()
        if username in users:
            return 'Username already exists'
        users[username] = password
        save_users(users)
        session['username'] = username
        return redirect(url_for('index'))
    return render_template('signup.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/send_message', methods=['POST'])
def send_message():
    if 'username' in session:
        message = request.form['message']
        messages = load_messages()
        messages.append({'username': session['username'], 'message': message})
        save_messages(messages)
        return '', 204
    return 'Unauthorized', 401

@app.route('/get_messages')
def get_messages():
    if 'username' in session:
        messages = load_messages()
        return jsonify(messages)
    return 'Unauthorized', 401

if __name__ == '__main__':
    if not os.path.exists('data'):
        os.makedirs('data')
    app.run(debug=True)
