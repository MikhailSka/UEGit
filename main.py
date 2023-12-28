from flask import Flask, jsonify
from generate_random_phrase import generate_random_phrase
import random

app = Flask(__name__)

# Sample meme texts
meme_texts = [
    "That moment when you find the last slice of pizza.",
    "When you finally understand a complex programming concept.",
    "When you realize it's Friday.",
    "When you see someone using Internet Explorer.",
    "When the code finally works after hours of debugging."
]

@app.route('/random-meme', methods=['GET'])
def get_random_meme():
    random_meme_text = random.choice(meme_texts)
    return jsonify({'meme_text': random_meme_text})

@app.route('/random-phrase', methods=['GET'])
def get_random_phrase():
    num_words = 3  
    random_phrase = generate_random_phrase(num_words)
    return jsonify({'random_phrase': random_phrase})

if __name__ == '__main__':
    app.run(debug=True)