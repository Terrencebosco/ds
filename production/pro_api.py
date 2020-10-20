########
# just keeping this incase we run into issues with the new api/flaskapp
########

from flask import Flask, request, jsonify
from flask_cors import CORS
import json
from pro_predict import predict_on_new
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
        user_input = request.json['input']

        # make prediction with input
        prediction = predict_on_new(user_input)

        # return prediction
        return(jsonify(prediction))

    return app

if __name__ == '__main__':
    APP = create_app()
    APP.run(debug=True, host="0.0.0.0", port=port)

    {'input':'car'}