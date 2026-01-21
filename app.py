from flask import Flask, render_template
import os  # <-- یہ line add کریں

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/cricket')
def cricket():
    return render_template('cricket.html')  # ICC Widget Page

@app.route('/football')
def football():
    return render_template('football.html')  # Football Widget Page

# =========================
# Render کے لیے یہ ضروری ہے
# =========================
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render کا dynamic PORT
    app.run(host="0.0.0.0", port=port)        # 0.0.0.0 = all network interfaces