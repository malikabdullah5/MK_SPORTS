from flask import Flask, render_template
import requests
import os

app = Flask(__name__)

# 🔑 CricketData API Key
API_KEY = "5a3ac28e-edf4-4df3-9941-9d4111fedbc9"

# 🏏 Get cricket matches from API
def get_matches():
    url = f"https://cricketdata.org/api/matches/?apikey={API_KEY}"
    try:
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            data = r.json()
            return data.get("data", [])  # ✅ Correct list
    except Exception as e:
        print("API Error:", e)
    return []

# 🏠 Home Page
@app.route("/")
def home():
    return render_template("home.html")

# 🏏 Cricket Page
@app.route("/cricket")
def cricket():
    matches = get_matches()

    live_matches = []
    upcoming_matches = []

    for m in matches:
        status = m.get("status", "").lower()

        if "live" in status:
            live_matches.append(m)
        elif "upcoming" in status or "scheduled" in status:
            upcoming_matches.append(m)

    return render_template(
        "cricket.html",
        live_matches=live_matches,
        upcoming_matches=upcoming_matches
    )

# ⚽ Football Page
@app.route("/football")
def football():
    return render_template("football.html")

# 🧪 Debug API (check raw data)
@app.route("/debug-api")
def debug_api():
    url = f"https://cricketdata.org/api/matches/?apikey={API_KEY}"
    r = requests.get(url)
    return r.json()

# 🚀 Run on Render
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)