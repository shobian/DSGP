from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/Home')
def Home():
    return render_template('Home.html')
@app.route('/')
@app.route('/Home')
def Home():
    return render_template('Home.html')
@app.route('/Quiz')
def Quiz():
    return render_template('Quiz.html')
@app.route('/signup')
def signup():
    return render_template('signup.html')
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/Aboutus')
def Aboutus():
    return render_template('Aboutus.html')
@app.route('/Contact')
def Contact():
    return render_template('Contact.html')
if __name__ == "__main__":
    app.run(debug=True)
