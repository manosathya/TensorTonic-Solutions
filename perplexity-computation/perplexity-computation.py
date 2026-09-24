import math

def perplexity(prob_distributions: list, actual_tokens: list) -> float:
    """
    Returns the sequence perplexity.
    """
    H_running = 0
    
    for i in range(len(actual_tokens)):
        H_running += math.log(prob_distributions[i][actual_tokens[i]])

    H = -H_running / len(actual_tokens)

    return math.exp(H)