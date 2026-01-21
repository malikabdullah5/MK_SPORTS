import os
import requests
from flask import Flask, render_template

app = Flask(__name__)

API_KEY = "5a3ac28e-edf4-4df3-9941-9d4111fedbc9"  # CricketData.org API key
API_URL = f"https://cricketdata.org/api/matches?apikey={API_KEY}"

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/cricket')
def cricket():
    response = requests.get(API_URL)
    if response.status_code == 200:
        matches = response.json()  # JSON data of live matches
    else:
        matches = []
    return render_template('cricket.html', matches=matches)

@app.route('/football')
def football():
    return render_template('football.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)