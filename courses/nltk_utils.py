import numpy as np
import nltk
from nltk.corpus import words
from spellchecker import SpellChecker
# nltk.download('punkt')
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()
spell = SpellChecker()
english_vocab = set(words.words())

def tokenize(sentence):
    # Split sentence into tokens
    tokens = nltk.word_tokenize(sentence)

    # Correct misspelled words
    corrected_tokens = set()
    for token in tokens:
        if token not in english_vocab:
            corrected_token = spell.correction(token)
            corrected_tokens.add(corrected_token)
        else:
            corrected_tokens.add(token)

    return list(corrected_tokens)

def stem(word):
    """
    stemming = find the root form of the word
    examples:
    words = ["organize", "organizes", "organizing"]
    words = [stem(w) for w in words]
    -> ["organ", "organ", "organ"]
    """
    if word is not None:
        return stemmer.stem(word.lower())
    else:
        return None

def bag_of_words(tokenized_sentence, words):
    """
    return bag of words array:
    1 for each known word that exists in the sentence, 0 otherwise
    example:
    sentence = ["hello", "how", "are", "you"]
    words = ["hi", "hello", "I", "you", "bye", "thank", "cool"]
    bog   = [  0 ,    1 ,    0 ,   1 ,    0 ,    0 ,      0]
    """
    # stem each word
    sentence_words = [stem(word) for word in tokenized_sentence]
    # initialize bag with 0 for each word
    bag = np.zeros(len(words), dtype=np.float32)
    for idx, w in enumerate(words):
        if w in sentence_words: 
            bag[idx] = 1

    return bag
