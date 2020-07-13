from flask import Flask
from flask_pymongo import PyMongo

def create_app(test_config=None):
    app = Flask(__name__)
    #secret key required for POST method
    app.secret_key = 'adjasnlnacwn2ne2queh398rn3f2e015'
    app.config['MONGO_URI'] = "mongodb://localhost:27017/Users"
    mongo = PyMongo(app)
    
    from . import urlshort
    app.register_blueprint(urlshort.bp)

    return app

