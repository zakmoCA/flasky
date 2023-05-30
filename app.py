from flask import Flask, jsonify
from datetime import datetime
import random
import json

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

# Flask server challenge
@app.route("/current_time/")
def current_time():
    now = datetime.now().strftime("%H:%M")
    return f"<p>The current time is: ${now}<p>"

# Flask API challenge
@app.route("/coinflip/")
def coin_flip():
    result = random.choice(["Heads", "Tails"])
    return jsonify({"result": result})