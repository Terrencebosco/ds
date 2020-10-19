########
# just keeping this incase we run into issues with the new api/flaskapp
########

from flask import Flask, request, jsonify
from flask_cors import CORS
import json
from old_predict import predict_on_new
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

    # gain inputs from html form
        user_input = request.json['input']
        # convert generateor object to list
        # user_input_list = list(user_input)
        # print(user_input)
        # slice list convert to proper type
        # text = int(user_input_list[0])

        prediction = predict_on_new(user_input)

        # # return prediction
        return(jsonify(prediction))

    return app

if __name__ == '__main__':
    APP = create_app()
    APP.run(debug=True, host="0.0.0.0", port=port)

    {'input':'car'}