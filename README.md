# emoji -_< 
AI emoji detect
![3](https://github.com/shidktbw/emoji/assets/112849918/88da9914-a1b9-4ee8-a320-f11f5c51e534)



The model was trained on the EmoBank dataset and can classify text into three categories: Positive, Negative, and Neutral.

# Usage
The application provides a simple web interface where you can input text to be analyzed. After submitting the text, the application will display the detected emotion: Positive, Negative, or Neutral.

The application uses a pre-trained TensorFlow model (yep.h5) to make predictions. The model was trained on the EmoBank dataset, which contains sentences annotated with valence scores. The scores range from 1 to 5, with 1 being the most negative and 5 being the most positive. The application classifies scores above 3 as positive, scores below 3 as negative, and scores equal to 3 as neutral.

The application also uses a tokenizer (tokenizer.pickle) to convert the input text into sequences of integers, which are then fed into the model.

