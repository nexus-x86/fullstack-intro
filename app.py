from flask import Flask, render_template, request, redirect, url_for, session
import json
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

DATA_FILE = 'data/users.json'

def load_users():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_users(users):
    with open(DATA_FILE, 'w') as f:
        json.dump(users, f)

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
        # You can implement message saving here (e.g., save to a file or database)
        print(f"{session['username']}: {message}")
        return '', 204
    return 'Unauthorized', 401

if __name__ == '__main__':
    app.run(debug=True)
