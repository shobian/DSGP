import re

import MySQLdb
from flask import Flask, render_template, url_for
from flask import Flask,render_template,request,url_for,session,redirect,flash
from flask_mysqldb import MySQL
import numpy as np
import pickle

app = Flask(__name__)
app.secret_key = 'xyzsdfg'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'dsgp'

mysql = MySQL(app)

profit_model = pickle.load(open("C:/Users/ADMIN/Desktop/IIT/Year 2 sem 2/CM 2603 - Data Science Group Project/DSGP/Final model/Profit prdiction/lin_model.pkl",'rb'))
success_model = pickle.load(open("C:/Users/ADMIN/Desktop/IIT/Year 2 sem 2/CM 2603 - Data Science Group Project/DSGP/Final model/Sucess prediction/Sucess_model.pkl",'rb'))

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/contact')
def contact_page():
    return render_template('contact.html')

@app.route('/quiz')
def quiz_page():
    return render_template('quiz.html')

@app.route("/predict", methods=["POST", "GET"])
def predict():
    profit_features = [int(request.form['randdspend']), int(request.form['administration']), int(request.form['marketingspend'])]
    final_features = [np.array(profit_features)]

    success_features = [int(request.form['totalfunding']), int(request.form['fundingrounds']), int(request.form['fundingduration']), int(request.form['category']), int(request.form['countrycode'])]
    final_features1 = [np.array(success_features)]

    print(final_features)
    print(final_features1)

    prediction = profit_model.predict(final_features)
    success_prediction = success_model.predict(final_features1)
    
    print(prediction)
    print(success_prediction)

    output = "{}".format(prediction)
    output1 = "{}".format(success_prediction)
    print(output)
    print(output1)

        
    randdspend = request.form['randdspend']
    administration = request.form['administration']
    marketingspend = request.form['marketingspend']
    totalfunding = request.form['totalfunding']
    fundingrounds = request.form['fundingrounds']
    fundingduration = request.form['fundingduration']
    category = request.form['category']
    countrycode = request.form['countrycode']
    Prediction = output
    

    if str(output1) == "[1]":
        Profit = " Busines will successed"
        
    else:
        Profit = "Busines most likelyto fail"
        
        
    return render_template('results.html', randdspend=randdspend, administration=administration, marketingspend=marketingspend, totalfunding=totalfunding,fundingrounds=fundingrounds,fundingduration=fundingduration,category=category,countrycode=countrycode,Prediction=Prediction,Profit=Profit)

  

    return render_template("quiz.html", pred="{}".format( output))

    

          
    
    


@app.route('/signup')
def signup_page():
    return render_template('signup.html')

@app.route('/results')
def result_page():
    return render_template('results.html')



@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route('/login', methods =['GET', 'POST'])
def login():
    mesage = ''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE email = % s AND password = % s', (email, password, ))
        user = cursor.fetchone()
        if user:
            session['loggedin'] = True
            session['name'] = user['name']
            session['email'] = user['email']
            mesage = 'Logged in successfully !'
            return render_template('quiz.html', mesage = mesage)
        else:
            mesage = 'Please enter correct email / password !'
    return render_template('login.html', mesage = mesage)



@app.route('/register', methods=['GET', 'POST'])
def register():
    mesage = ''
    if request.method == 'POST' and 'name' in request.form and 'email' in request.form and 'age' in request.form and 'companyname' in request.form and 'businessnature' in request.form and 'password' in request.form:
        name = request.form['name']
        email = request.form['email']
        age = request.form['age']
        companyname = request.form['companyname']
        businessnature = request.form['businessnature']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE email = % s', (email,))
        account = cursor.fetchone()
        if account:
            mesage = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            mesage = 'Invalid email address !'
        elif not name or not password or not email:
            mesage = 'Please fill out the form !'
        else:

            cursor.execute('INSERT INTO user VALUES (%s, % s, % s, % s, % s, % s)', (name, email, age,companyname,businessnature,password,))
            mysql.connection.commit()
            mesage = 'You have successfully registered !'
            return render_template('login.html', mesage=mesage)
    elif request.method == 'POST':
        mesage = 'Please fill out the form !'

    return render_template('signup.html')


if __name__ == "__main__":
    app.run(debug=True)