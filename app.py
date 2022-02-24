from flask import Flask
from flask_mobility import Mobility


app = Flask(__name__)
Mobility(app)
