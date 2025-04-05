import spacy
import re

nlp = spacy.load("en_core_web_sm")

def extract_joined_phrase(text):
    segments = re.split(r'[,.]', text)
    all_words = []

    for segment in segments:
        doc = nlp(segment)
        words = []

        for token in doc:
            if token.dep_ == "neg":
                words.append(token.text)
                continue

            if token.tag_ == "VBG" or token.pos_ in ["NOUN", "VERB", "ADJ"]:
                words.append(token.text)

        all_words.extend(words[:5])

    return " ".join(all_words)