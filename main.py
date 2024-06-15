import flask

# Create the app using flask as a framework
app = flask.Flask(__name__)

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
@app.route("/login", methods=["GET"])
def login():
    return flask.render_template("app/login.html")


# Chat
@app.route("/chat", methods=["GET"])
def chat():
    return flask.render_template("app/chat.html")


# Signup sectoin
@app.route("/signup", methods=["GET"])
def signup():
    return flask.render_template("app/signup.html")

# Run the python app!
if __name__ == "__main__":
    app.run(debug=True)