import re
import nltk
from nltk.corpus import words
from nltk.metrics import edit_distance

nltk.download('words')

english_words = set(words.words())


def tokenize(text):
    return re.findall(r'\w+', text.lower())


def generate_candidates(word):
    candidates = []
    for candidate in english_words:
        if edit_distance(word, candidate) <= 2:
            candidates.append(candidate)
    return candidates


def auto_correct(input_text):
    tokens = tokenize(input_text)
    corrected_tokens = []

    for token in tokens:
        if token in english_words:
            corrected_tokens.append(token)
        else:
            candidates = generate_candidates(token)
            if candidates:
                best_candidate = max(candidates, key=lambda c: edit_distance(token, c))
                corrected_tokens.append(best_candidate)
            else:
                corrected_tokens.append(token)

    return ' '.join(corrected_tokens)


input_text = input("Enter a sentence: ")
corrected_text = auto_correct(input_text)
print("Corrected text:", corrected_text)
