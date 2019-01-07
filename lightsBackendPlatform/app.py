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

