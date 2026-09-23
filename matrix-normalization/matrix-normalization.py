import numpy as np

    
def matrix_normalization(matrix: list, axis=None, norm_type: str = "l2") -> np.ndarray:
    """
    Returns a NumPy array with the same shape as matrix.
    """
    matrix = np.asarray(matrix, dtype=float)

    if norm_type == "l1":
        norm_factor = np.sum(np.abs(matrix), axis=axis, keepdims=True)
    elif norm_type == "l2":
        norm_factor = np.sqrt(np.sum(matrix**2, axis=axis, keepdims=True))
    elif norm_type == "max":
        norm_factor = np.max(np.abs(matrix), axis=axis, keepdims=True)
    else:
        raise ValueError("norm_type must be 'l1', 'l2', or 'max'")

    # Avoid division by zero
    norm_factor = np.where(norm_factor == 0, 1, norm_factor)

    return matrix / norm_factor
        

        