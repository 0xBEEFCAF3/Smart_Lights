import sys
from flask import Flask
from flask import render_template
sys.path.insert(0, '../lightsAPI/src')
from lightsAPI import lightsAPI
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'

lightsAPI = lightsAPI(7,5,3)

@app.route("/")
@cross_origin()
def index():
	print("hit end point")
	return render_template('index.html')


@app.route("/greenify")
@cross_origin()
def greenify():
	lightsAPI.greenify_lights()
	return "200 OK"

@app.route("/blueify")
@cross_origin()
def blueify():
        lightsAPI.blueify_lights()
        return "200 OK"

@app.route("/redify")
@cross_origin()
def redify():
        lightsAPI.redify_lights()
        return "200 OK"

@app.route("/yellowify")
@cross_origin()
def yellowify():
        lightsAPI.yellowify_lights()
        return "200 OK"

@app.route("/magentify")
@cross_origin()
def magentify():
        lightsAPI.magentify_lights()
        return "200 OK"

@app.route("/cyanify")
@cross_origin()
def cyanify():
        lightsAPI.cyanify_lights()
        return "200 OK"


@app.route("/rgb/<r>/<g>/<b>")
@cross_origin()
def rgb(r, g, b):
        lightsAPI.set_duty_cycle(r, g, b)
#        lightsAPI.set_all_colors(r,g,b)
	return "200 OK"



@app.route("/off")
@cross_origin()
def off():
        lightsAPI.clean_up()
        return "200 OK"

@app.route("/on")
@cross_origin()
def on():
	lightsAPI.init_lights()
	return "200 OK"
