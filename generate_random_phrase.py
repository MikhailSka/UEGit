import random

def generate_random_phrase(num_words=3):
    default_word_list = [
        "apple", "banana", "orange", "grape", "kiwi",
        "melon", "pear", "peach", "plum", "berry",
        "cherry", "lemon", "lime", "pineapple", "mango",
        "strawberry", "watermelon", "blueberry", "raspberry", "blackberry",
        "peanut", "almond", "cashew", "walnut", "pecan"
    ]

    if num_words < 1:
        raise ValueError("Number of words should be greater than or equal to 1")

    random_words = random.sample(default_word_list, min(num_words, len(default_word_list)))
    random_phrase = ' '.join(random_words)
    return random_phrase

random_phrase = generate_random_phrase()