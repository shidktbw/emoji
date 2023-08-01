from flask import Flask, render_template, request
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle

app = Flask(__name__)

# load model
model = tf.keras.models.load_model('yep.h5')

# load tokenizer
with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)
    
# main
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        new_text = [request.form.get('text')]

        new_sequences = tokenizer.texts_to_sequences(new_text)
        new_padded_sequences = pad_sequences(new_sequences, padding='post', maxlen=117)

        predictions = model.predict(new_padded_sequences)

        valence = predictions[0][0]
        if valence > 3:
            emotion = 'Positive'
        elif valence < 3:
            emotion = 'Negative'
        else:
            emotion = 'Neutral'

        return render_template('index.html', emotion=emotion)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
