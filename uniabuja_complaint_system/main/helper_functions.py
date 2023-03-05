import re
import os
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import HashingVectorizer


stop = stopwords.words('english')

def tokenizer(text):
    """to remove stop words or puntuations form corpos"""
    text = re.sub('<[^>]*>', '', text)
    emoticons = re.findall('(?::|;|=)(?:-)?(?:\)|\(|D|P)', text.lower())
    text = re.sub('[\W]+', ' ', text.lower()) +\
        ' '.join(emoticons).replace('-', '')
    tokenized = [w for w in text.split() if w not in stop]
    return tokenized

vect = HashingVectorizer(decode_error='ignore',
                         n_features=2**21,
                         preprocessor=None,
                         tokenizer=tokenizer
                        )

