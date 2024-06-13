from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# In-memory storage for users and messages (for simplicity)
users = {'user1': 'password1', 'user2': 'password2'}
messages = []

@app.route('/')
def index():
    if 'username' in session:
        return redirect(url_for('chat'))
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username in users and users[username] == password:
        session['username'] = username
        return redirect(url_for('chat'))
    return 'Invalid credentials'

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/chat')
def chat():
    if 'username' in session:
        return render_template('chat.html', username=session['username'])
    return redirect(url_for('index'))

@app.route('/send_message', methods=['POST'])
def send_message():
    if 'username' in session:
        message = request.form['message']
        messages.append({'username': session['username'], 'message': message, 'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
        return jsonify({'status': 'success'})
    return jsonify({'status': 'not_logged_in'})

@app.route('/get_messages')
def get_messages():
    return jsonify(messages)

if __name__ == '__main__':
    app.run(debug=True)
