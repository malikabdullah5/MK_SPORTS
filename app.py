from flask import Flask, render_template
import requests
import os

app = Flask(__name__)

# Your CricketData API key
API_KEY = "5a3ac28e-edf4-4df3-9941-9d4111fedbc9"

# URLs for live and upcoming matches
LIVE_URL = f"https://cricketdata.org/api/matches?apikey={API_KEY}"
UPCOMING_URL = f"https://cricketdata.org/api/upcoming?apikey={API_KEY}"

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/cricket')
def cricket():
    # Fetch live matches
    live_matches = []
    upcoming_matches = []
    try:
        live_resp = requests.get(LIVE_URL)
        if live_resp.status_code == 200:
            live_matches = live_resp.json()
    except:
        live_matches = []

    try:
        upcoming_resp = requests.get(UPCOMING_URL)
        if upcoming_resp.status_code == 200:
            upcoming_matches = upcoming_resp.json()
    except:
        upcoming_matches = []

    return render_template('cricket.html', live_matches=live_matches, upcoming_matches=upcoming_matches)

@app.route('/football')
def football():
    return render_template('football.html')  # Placeholder

# Important: Render needs host 0.0.0.0 and dynamic port
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)