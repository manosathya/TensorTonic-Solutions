import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    A = np.asarray(A)

    if len(A) == 0:
        return A

        
    rows, cols = len(A), len(A[0])

    A_T = np.zeros((cols,rows))

    for i in range(rows):
        for j in range(cols):
            A_T[j][i] = A[i][j]

    return A_T