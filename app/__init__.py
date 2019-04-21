from flask import Flask
from flask_bootstrap import Bootstrap

#Initialize Flask Extensions
bootstrap = Bootstrap()

def create_app(config_name):
    app = Flask(__name__)

    #Initialize flask extensions
    bootstrap.init_app(app)

    return app