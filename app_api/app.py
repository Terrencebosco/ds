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
        return(flask.render_template('base.html'))

    @app.route('/predict', methods=['POST'])
    def predict_sub():
        text = flask.request.form.values()
        text_list = list(text)
        prediction = predict_on_new((text_list[0]))
        return(flask.render_template('base.html',prediction_text=prediction))

    return app

if __name__ == '__main__':
    APP = create_app()
    APP.run(debug=True, host="0.0.0.0", port=port)

        # text = string_from_web = '''Was in Vegas this weekend and hit up Speed Vegas. My plan
        # originally was to drive the C8 but this time I could afford the Ferrari so I
        # went with that and I don't regret my decision at all. Driving a Ferrari was a
        # childhood dream come true and its something I'll never forget as long as I live.
        # The car was super easy to drive and get used to. After the first lap I felt right
        # at home with how it drove. Hitting those turns at 55-60mph without having to
        # brake or put the gas was amazing. This car handled those turns like a champ and
        # I was shocked at how good it was at taking those turns. On the straight-away I
        # hit 142mph and it got up to that speed super quick. The sound of the engine right
        # behind your head screaming as your floor it is something that you gotta hear.'''


        # return(predict_on_new(text))
        #return(json.dumps({'input':'test', 'predict':'r/AdviceAnimals'}))