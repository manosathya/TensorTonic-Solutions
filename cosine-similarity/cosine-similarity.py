import numpy as np

    
def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    a, b = np.asarray(a), np.asarray(b)
    norm_product = np.linalg.norm(a) * np.linalg.norm(b)

    if norm_product == 0:
        return 0.0
    
    return float(np.dot(a,b) / norm_product)
