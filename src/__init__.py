from flask import Flask

app = Flask(__name__, template_folder='views')

from src.controllers import *
from src.routes import *

app.config['SECRET_KEY'] = 'test-flask'

def start_app():
    app.run(port = 5000, debug=True)