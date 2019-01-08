import sys
from flask import Flask
sys.path.insert(0, '../lightsAPI/src')
from lightsAPI import lightsAPI


app = Flask(__name__)

lightsAPI = lightsAPI(7,5,3)

@app.route("/")
def ping():
    return "Pong!"


@app.route("/greenify")
def greenify():
	lightsAPI.greenify_lights()
	return "200 OK"

@app.route("/blueify")
def blueify():
        lightsAPI.blueify_lights()
        return "200 OK"

@app.route("/redify")
def redify():
        lightsAPI.redify_lights()
        return "200 OK"

@app.route("/rgb/<r>/<g>/<b>")
def rgb(r, g, b):
        lightsAPI.set_duty_cycle(r, g, b)
#        lightsAPI.set_all_colors(r,g,b)
	return "200 OK"

@app.route("/off")
def off():
        lightsAPI.clean_up()
        return "200 OK"
@app.route("/on")
def on():
	lightsAPI.init_lights()
	return "200 OK"
