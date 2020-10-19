import flask
from flask_cors import CORS
import json
from predict import predict_on_new, json_to_list
from os import getenv

port = int(getenv("PORT", 5000))

def create_app():
    """create instance of our flask app"""
    app = flask.Flask(__name__)
    CORS(app)

    @app.route('/')
    def root():
        return(flask.render_template('base.html'))

    @app.route('/about')
    def about():
        return(flask.render_template('about.html'))

    @app.route('/predict', methods=['POST'])
    def predict_sub():
        '''
        Create route for prediction of of user text that can be used to make a
        prediction.

        user inputs text, and int
            text: series of string objects
            int: none 0 number from 1 to 20.
        '''

        # gain inputs from html form
        user_input = request.form['input']

        # convert generateor object to list
        user_input_list = list(user_input)

        ## slice list convert to proper type
        num = int(user_input_list[1])
        text = str(user_input_list[0])

        # predict
        prediction = predict_on_new(text, num)

        prediction_list = json_to_list(prediction)

        # return prediction
        return(flask.render_template('base.html',prediction_text=prediction_list))

    return app

if __name__ == '__main__':
    APP = create_app()
    APP.run(debug=True, host="0.0.0.0", port=port)

        # text = '''Was in Vegas this weekend and hit up Speed Vegas. My plan
        # originally was to drive the C8 but this time I could afford the Ferrari so I
        # went with that and I don't regret my decision at all. Driving a Ferrari was a
        # childhood dream come true and its something I'll never forget as long as I live.
        # The car was super easy to drive and get used to. After the first lap I felt right
        # at home with how it drove. Hitting those turns at 55-60mph without having to
        # brake or put the gas was amazing. This car handled those turns like a champ and
        # I was shocked at how good it was at taking those turns. On the straight-away I
        # hit 142mph and it got up to that speed super quick. The sound of the engine right
        # behind your head screaming as your floor it is something that you gotta hear.'''

         # print('---')
                    # print(user_input_list[0],type(user_input_list[0]))
                    # print('---')
                    # print(num, type(num))
                    # print('---')
                    # return(flask.render_template('base.html'))

        # return(predict_on_new(text))
        #return(json.dumps({'input':'test', 'predict':'r/AdviceAnimals'}))