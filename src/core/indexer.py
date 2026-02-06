import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

def generate_semantic_index(corpus_data):
    """
    Converts raw legal text into weighted semantic vectors.
    """
    vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
    embedding_matrix = vectorizer.fit_transform(corpus_data)
    return embedding_matrix, vectorizer