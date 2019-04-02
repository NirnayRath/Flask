#My first flask app
import os
from flask import Flask

def create_app():
    """Create and configure an instance of the Flask app"""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite')
        )
    if test_config is None:
        app.config.from_pyfile('config.py',silent=True)
    else:
        app.config.from_mapping(test_config)


    try:
        os.makedir(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def hello():
        return "hello World!!"

    return app