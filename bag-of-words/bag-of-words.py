import numpy as np
from collections import Counter
def bag_of_words_vector(tokens: list, vocab: list) -> np.ndarray:
    """
    Returns a NumPy array with length len(vocab).
    """
    token_count = Counter(tokens)

    bow = np.zeros(len(vocab), dtype=int)

    for i, word in enumerate(vocab):
        bow[i] = token_count[word]

    return bow