import numpy as np

def pad_sequences(seqs: list, pad_value: int = 0, max_len: int | None = None) -> np.ndarray:
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    if len(seqs) == 0:
        return np.empty((0,0), dtype=int)
        
    if max_len is None:
        L = max([len(x) for x in seqs]) 
    else:
        L = max_len

    out = np.full((len(seqs), L), pad_value)
    
    for i,seq in enumerate(seqs):
        end = min(len(seq), L)
        out[i][:end] = seq[:end]

    return out