from flask import Flask, request
from flask_cors import CORS
import json
from pro_predict import predict_on_new, json_to_list, pred_to_json
from os import getenv

port = int(getenv("PORT", 5000))

def create_app():
    """create instance of our flask app"""
    app = Flask(__name__)
    CORS(app)

    @app.route('/')
    def root():
        return 'hello'

    @app.route('/predict', methods=['POST'])
    def predict_sub():

        # request json from front end.
        user_input = request.json['text']

        # make prediction with input
        prediction = predict_on_new(user_input)

        #slice prediction and return dict with json.dumps()
        json_prediction = pred_to_json(prediction)

        return json_prediction

    return app

if __name__ == '__main__':
    APP = create_app()
    APP.run(host="0.0.0.0", port=port)