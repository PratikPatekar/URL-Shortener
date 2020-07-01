from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__)
    #secret key required for POST method
    app.secret_key = 'adjasnlnacwn2ne2queh398rn3f2e015'

    from . import urlshort
    app.register_blueprint(urlshort.bp)

    return app

