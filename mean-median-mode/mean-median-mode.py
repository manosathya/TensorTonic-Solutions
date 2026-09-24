from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    x = np.asarray(sorted(x))
    n = len(x)

    if n % 2 == 0:
        median = (x[n // 2 - 1] + x[n // 2]) / 2
    else:
        median = x[n // 2]

    mode = Counter(x).most_common(1)[0][0]

    return {
        "mean": float(np.mean(x)),
        "median": float(median),
        "mode": float(mode)
    }