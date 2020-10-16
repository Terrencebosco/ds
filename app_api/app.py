import flask
from flask_cors import CORS
import json #jsonify?, requests?, cors?

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

