from flask import Flask, render_template

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

if __name__ == "__main__":
    app.run(debug=True)