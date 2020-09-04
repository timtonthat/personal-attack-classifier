import pickle
import unidecode
import re
import json
from flashtext import KeywordProcessor
from tensorflow.python.keras.preprocessing.sequence import pad_sequences

with open("attack_classifier/assets/tokenizer.pickle", "rb") as handle:
    tokenizer = pickle.load(handle)


def standardize(word):
    return unidecode.unidecode(word.lower())


with open("attack_classifier/assets/contractions.txt") as json_file:
    contraction_mapper = json.load(json_file)

contraction_processor = KeywordProcessor()

for k, v in contraction_mapper.items():
    contraction_processor.add_keyword(k, v)


def replace_contraction(text):
    return contraction_processor.replace_keywords(text)


def remove_non_alpha(text):
    regex = re.compile("[^a-zA-Z\s]")
    return regex.sub("", text)


def tokenize(text):
    tokens = text.split(" ")
    tokens = [t for t in tokens if t != ""]
    return tokens


def clean_text(text):
    text = standardize(text)
    text = replace_contraction(text)
    text = remove_non_alpha(text)
    return text


def process_text(text):
    tokens = [tokenize(text)]
    sequence = tokenizer.texts_to_sequences(tokens)
    padded_sequence = pad_sequences(sequence, maxlen=max_length, padding="post")
    return padded_sequence


max_length = 55


class TextProcessor:

    tokenizer = tokenizer

    @staticmethod
    def process(text):
        """
        Clean text and transform into a vector
        """
        cleaned_text = clean_text(text)
        padded_sequence = process_text(cleaned_text)
        return padded_sequence
