from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('landing.html')

@app.route('/community')
def community_page():
    return render_template("community.html")

@app.route('/consult')
def consultance_page():
    return render_template("consult.html")

@app.route('/self-care')
def care_page():
    return render_template("selfcare.html")

@app.route('/test')
def test_page():
    return render_template("test.html")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')