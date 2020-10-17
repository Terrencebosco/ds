import pandas as pd
import numpy as np
import pickle
from collections import OrderedDict
import json
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import load_model

# Read in tier 1 and tier 2 category lookup data
subreddit_info = pd.read_csv('model/subreddit_info_cleaned.csv')

# Load serialized model
restored_model = load_model('model/keras_pred_subreddit_model_v5.h5')

# Load serialized tokenizer
with open('model/keras_tokenizer_v5.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

# Load serialized label encoder
with open('model/sklearn_label_encoder_v5.pickle', 'rb') as handle:
    encoder = pickle.load(handle)

maxlen = 250 # DO NOT MODIFY THIS

def predict_on_new(input, tokenizer=tokenizer, restored_model=restored_model,
                   maxlen=maxlen, encoder=encoder):
    '''This function takes an input as a string (Web will hit our API endpoint)
    and returns (in JSON format) the top five subreddit predictions along with
    each subreddit's tier 1 and tier 2 categories'''
    seq = tokenizer.texts_to_sequences([input])
    pad_seq = sequence.pad_sequences(seq, maxlen=maxlen)
    pred = restored_model.predict(pad_seq)
    class_names = list(encoder.inverse_transform(pred[0].argsort()[-5:][::-1]))

    t1_category = []
    t2_category = []

    pred_key = ['pred_1', 'pred_2', 'pred_3', 'pred_4', 'pred_5']

    for c in class_names:
        for i, sub_red in enumerate(subreddit_info['subreddit']):
            if sub_red == c:
                t1_cat = subreddit_info['category_1'].iloc[i]
                t1_category.append(t1_cat)
                t2_cat = subreddit_info['category_2'].iloc[i]
                t2_category.append(t2_cat)

            pred_dict = OrderedDict(zip(pred_key, zip(class_names, zip(t1_category, t2_category))))
    return json.dumps(pred_dict)

if __name__ == "__main__":
    string_from_web = '''Was in Vegas this weekend and hit up Speed Vegas. My plan
    originally was to drive the C8 but this time I could afford the Ferrari so I
    went with that and I don't regret my decision at all. Driving a Ferrari was a
    childhood dream come true and its something I'll never forget as long as I live.
    The car was super easy to drive and get used to. After the first lap I felt right
    at home with how it drove. Hitting those turns at 55-60mph without having to
    brake or put the gas was amazing. This car handled those turns like a champ and
    I was shocked at how good it was at taking those turns. On the straight-away I
    hit 142mph and it got up to that speed super quick. The sound of the engine right
    behind your head screaming as your floor it is something that you gotta hear.'''

#     string_from_web = '''PandasGUI is a project for EDA in Pandas that I have been working on a while now and finally feel ready to share here. I use this a lot for my own data analysis and hope it will help others too!

# I was inspired to make this after using applications like Excel, Tableau and JMP and finding them quicker than Pandas for basic ad hoc viewing, plotting and reshaping. PandasGUI aims to make basic EDA easy but also allows you to easily move DataFrames in memory between the GUI and IPython so you still have the full power of Pandas. It's made with PyQt5 and renders in a standalone window compatible with any IDE.'''

    # Prediction JSON returned to web
    print(predict_on_new(string_from_web))

