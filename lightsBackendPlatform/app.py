#!/usr/bin/python3
import sys
from flask import Flask
from flask import render_template
from threading import Thread

sys.path.insert(0, '../lightsAPI/src')
from lightsAPI import lightsAPI
#from flask_cors import CORS, cross_origin

app = Flask(__name__)
#cors = CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'

lightsAPI = lightsAPI(24,5,12)
rainbow_thread = Thread(target = lightsAPI.rainbow_lights, args=([0.005]))         
rainbow_thread.daemon = True
rainbow_thread_extra = Thread(target = lightsAPI.rainbow_lights, args=([0.010]))         
rainbow_thread_extra.daemon = True



@app.route("/")
#@cross_origin()
def index():
        return render_template('index.html')


@app.route("/greenify")
#@cross_origin()
def greenify():
        lightsAPI.return_to_main = True
        lightsAPI.greenify_lights()
        return "200 OK"

@app.route("/blueify")
#@cross_origin()
def blueify():
        lightsAPI.return_to_main = True
        lightsAPI.blueify_lights()
        return "200 OK"

@app.route("/redify")
#@cross_origin()
def redify():
        lightsAPI.return_to_main = True
        lightsAPI.redify_lights()
        return "200 OK"

@app.route("/yellowify")
#@cross_origin()
def yellowify():
        lightsAPI.return_to_main = True
        lightsAPI.yellowify_lights()
        return "200 OK"

@app.route("/magentify")
#@cross_origin()
def magentify():
        lightsAPI.return_to_main = True
        lightsAPI.magentify_lights()
        return "200 OK"

@app.route("/cyanify")
#@cross_origin()
def cyanify():
        lightsAPI.return_to_main = True
        lightsAPI.cyanify_lights()
        return "200 OK"


@app.route("/rgb/<r>/<g>/<b>")
#@cross_origin()
def rgb(r, g, b):
        lightsAPI.return_to_main = True
        lightsAPI.set_green_light(g)
        lightsAPI.set_red_light(r)
        lightsAPI.set_blue_light(b)
        return "200 OK"


@app.route("/rainbow")
#@cross_origin()
def rainbow():
    lightsAPI.return_to_main = False
    if not rainbow_thread.isAlive():
        rainbow_thread.start()

        return "200 OK"

@app.route("/exrainbow")
def exrainbow():
        lightsAPI.return_to_main = False
        #lightsAPI.rainbow_lights(1)
        if not rainbow_thread_extra.isAlive():
            rainbow_thread_extra.start();

        return "200 OK"

@app.route("/off")
#@cross_origin()
def off():
        lightsAPI.return_to_main = True
        lightsAPI.clean_up()
        return "200 OK"

@app.route("/on")
#@cross_origin()
def on():
        lightsAPI.return_to_main = True
        lightsAPI.init_lights()
        return "200 OK"
