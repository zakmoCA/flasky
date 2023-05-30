from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello World!<p>"

@app.route("/goodbye/")
def goodbye_world():
    return "<p>Goodbye, World!</p>"

@app.route("/coder/")
def coder():
    return "<p>This web app was created in a class at Coder Academy.</p>"


@app.route("/current_time/")
def current_time():
    now = datetime.now().strftime("%H:%M")
    return f"<p>The current time is: ${now}<p>"