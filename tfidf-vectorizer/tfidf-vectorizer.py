import math
from collections import Counter
import numpy as np
from collections import defaultdict

def tfidf_vectorizer(documents: list[str]) -> dict:
    """
    Returns a dictionary with tfidf_matrix and vocabulary.
    """

    tf = {}
    df = defaultdict(int)
    doc_len = len(documents)
    #idf = defaultdict(int)
    
    #tf 

    for i,doc in enumerate(documents):
        tf[i] = defaultdict(int)
        doc_tok = doc.strip().lower().split(" ")
        tok_log = set()
        
        for tok in doc_tok:
            tf[i][tok] += 1 / len(doc_tok)
            if tok not in tok_log:
                df[tok] += 1
                tok_log.add(tok)

    vocab = sorted(df.keys())
    tf_idf = np.zeros((doc_len,len(vocab)))

    idx = 0
    for i, tok in enumerate(vocab):
        #idf[tok] = log((i+1)/df[tok])
        idf = np.log((doc_len)/df[tok])

        for doc in range(doc_len):
            tf_idf[doc][i] = tf[doc].get(tok, 0) * idf
            
        
    return {"tfidf_matrix" : tf_idf, "vocabulary" : vocab}            
            

