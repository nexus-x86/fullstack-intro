import flask
import json
import base64

# Create the app using flask as a framework
app = flask.Flask(__name__)
app.secret_key = "hawkchat123!!!"

# .json Database
data = {}
file = open("data/users.json", "r+")


# Database methods
def load_file():
    global data # reference global data var
    file.seek(0)
    data = json.loads(file.read())

def save_file():
    # go to beginning of file and clear
    file.seek(0)
    file.truncate()

    # write contents
    file.write(json.dumps(data))
    file.flush()

def error(msg):
    return "?error=" + base64.b64encode(msg.encode("ascii")).decode("ascii")

# Our static routes/pages
# Index pgae (first page the user sees)
@app.route("/", methods=["GET"])
def index():
    return flask.render_template("index.html")

# About page
@app.route("/about-us", methods=["GET"])
def about():
    return flask.render_template("about.html")

# TOS page
@app.route("/termsofservice", methods=["GET"])
def tos():
    return flask.render_template("tos.html")

# Licensing page
@app.route("/licensing", methods=["GET"])
def license():
    return flask.render_template("license.html")

# Github source redirect
@app.route("/source", methods=["GET"])
def source():
    return flask.redirect("https://github.com/nexus-x86/fullstack-intro/tree/main")


# Login section
@app.route("/login", methods=["POST", "GET"])
def login():
    # initialize users
    if not ("users" in data):
        data["users"] = {}
        save_file()

    if flask.request.method == "POST":
        uname = flask.request.json["username"]
        pwd = flask.request.json["password"]

        load_file()

        # log in
        if uname in data["users"]:
            if data["users"][uname] == pwd:
                flask.session["username"] == uname
                return flask.redirect(flask.url_for("chat"))
        
        return flask.redirect(flask.url_for("login") + error("Account not found"))

    elif flask.request.method == "GET":
        # redirect to chat if already logged in
        if flask.session.get("username") in data["users"]:
            return flask.redirect(flask.url_for("chat"))
        
        # send login if not logged in
        return flask.render_template("app/login.html")

# Signup sectoin
@app.route("/signup", methods=["POST", "GET"])
def signup():
    # initialize users
    if not ("users" in data):
        data["users"] = {}
        save_file()

    if flask.request.method == "POST":
        uname = flask.request.json["username"]
        pwd = flask.request.json["password"]

        load_file()

        # already exists
        if uname in data["users"]:
            return flask.redirect(flask.url_for("signup") + error("Account already exists"))
        
        data[uname] = pwd

        save_file()

        flask.session["username"] = uname
        return flask.redirect(flask.url_for("chat"))
        

    elif flask.request.method == "GET":
        # redirect to chat if already logged in
        if flask.session.get("username") in data["users"]:
            return flask.redirect(flask.url_for("chat"))
        
        # send signup if not logged in
        return flask.render_template("app/signup.html")


# Chat
@app.route("/chat", methods=["GET"])
def chat():
    return flask.render_template("app/chat.html")


# Run the python app!
if __name__ == "__main__":
    app.run(port=3000, debug=True)