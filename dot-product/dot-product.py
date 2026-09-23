import numpy as np

def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """
    assert len(x) == len(y)

    res = 0

    for i,j in zip(x,y):
        res+= i*j

    return float(res)