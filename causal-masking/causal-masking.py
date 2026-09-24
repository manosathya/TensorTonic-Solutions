import numpy as np

def apply_causal_mask(scores: list, mask_value: float = -1e9) -> np.ndarray:
    """
    Returns a causally masked NumPy array matching the shape of scores.
    """
    scores = np.asarray(scores, dtype=float)

    assert scores.ndim >= 2
    assert scores.shape[-1] == scores.shape[-2]

    T = scores.shape[-1]
    mask = np.triu(np.ones((T, T), dtype=bool), k=1)
    
    
    return np.where(mask, mask_value, scores)