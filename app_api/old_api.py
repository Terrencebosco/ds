########
# just keeping this incase we run into issues with the new api/flaskapp
########

import flask
from flask_cors import CORS
import json
from predict import predict_on_new
from os import getenv

port = int(getenv("PORT", 5000))

def create_app():
    """create instance of our flask app"""
    app = flask.Flask(__name__)
    CORS(app)

    @app.route('/')
    def root():
        return 'hello'

    @app.route('/predict', methods=['POST'])
    def predict_sub():

        return(json.dumps({'input':'test', 'predict':'r/AdviceAnimals'}))

    return app

if __name__ == '__main__':
    APP = create_app()
    APP.run(host="0.0.0.0", port=port)