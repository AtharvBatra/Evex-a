from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('main.html')

@app.route('/community')
def community_page():
    return "in progress"

@app.route('/consult')
def consultance_page():
    return "in progress"

@app.route('/self-care')
def care_page():
    return "in progress"

if __name__ == "__main__":
    app.run(debug=True)