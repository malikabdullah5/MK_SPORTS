from flask import Flask, render_template
import requests

app = Flask(__name__)

API_KEY = "5a3ac28e-edf4-4df3-9941-9d4111fedbc9"  # آپ کا CricketData API key

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/cricket')
def cricket():
    url = f"https://cricketdata.org/api/matches?apikey={API_KEY}"
    try:
        response = requests.get(url)
        live_matches = response.json()
    except:
        live_matches = []  # اگر API fail ہو جائے تو empty list
    return render_template('cricket.html', live_matches=live_matches)

if __name__ == "__main__":
    app.run(debug=True)