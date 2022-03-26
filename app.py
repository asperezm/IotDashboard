from flask import Flask, render_template, jsonify, redirect, request
import json, base64
import person
import random
from datetime import datetime

app = Flask(__name__)

logged_in = {}
api_loggers = {}


@app.route("/login", methods=['GET', 'POST'])
def login():
    error = ""
    if request.method == 'POST':
        user = person.user(request.form['username'], request.form['password'])
        if user.authenticated:
            user.session_id = "str(binascii.b2a_hex(os.urandom(15)))"
            logged_in[user.username] = {"object": user}
            return redirect('/overview/{}/{}'.format(request.form['username'], user.session_id))
        else:
            error = "invalid Username or Passowrd"
       
    return render_template('Login.htm', error=error)
    
#this link is for the main dashboard of the website
@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.htm', title='HOME - Landing Page')

@app.route('/overview/<string:username>/<string:session>', methods=['GET', 'POST'])
def overview(username, session):
    
    global logged_in

    if username in logged_in and (logged_in[username]['object'].session_id == session):
        user = {
            "username" : username,
            "image":"/static/images/amanSingh.jpg",
            "api": "logged_in[username].api",
            "session" : session
        }

        devices = [
            {"Dashboard" : "device1",
            "deviceID": "Device1"
            }
        ]
        return render_template('overview.htm', title='Overview', user=user, devices=devices, temperature=get_temperature())
    
    else:
        return redirect('/login')
        
@app.route('/logout/<string:username>/<string:session>', methods=['GET', 'POST'])
def logout(username, session):
    
    global logged_in

    if username in logged_in and (logged_in[username]['object'].session_id == session):
        logged_in.pop(username)
        # print("logged out")
        return redirect('/')
    else:
        return redirect('/login')

@app.route("/api/<string:apikey>/temperature", methods=["GET", "POST"])
def get_temperature():
    randData = random.randint(15, 55)
    time = datetime.now()
    time = time.strftime("%H:%M:%S")
    response = {}
    response['time'] = time
    response['temperature'] = randData
    return response

@app.route("/api/<string:apikey>/moisture", methods=["GET", "POST"])
def get_moisture():
    randData = random.randint(0, 100)
    time = datetime.now()
    time = time.strftime("%H:%M:%S")
    response = {}
    response['time'] = time
    response['moisture'] = randData
    return response

@app.route("/api/<string:apikey>/humidity", methods=["GET", "POST"])
def get_humidity():
    randData = random.randint(0, 100)
    time = datetime.now()
    time = time.strftime("%H:%M:%S")
    response = {}
    response['time'] = time
    response['humidity'] = randData
    return response

@app.route("/api/<string:apikey>/light", methods=["GET", "POST"])
def get_light():
    randData = random.randint(300, 1000)
    time = datetime.now()
    time = time.strftime("%H:%M:%S")
    response = {}
    response['time'] = time
    response['light'] = randData
    return response


if __name__ == "__main__":
    app.run(debug=True)


