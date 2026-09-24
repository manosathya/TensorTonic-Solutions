def text_chunking(tokens: list, chunk_size: int, overlap: int) -> list:
    """
    Returns fixed-size token chunks with the requested overlap.
    """
    step_size = chunk_size - overlap

    l = 0
    output = []
    
    while l < len(tokens) - overlap:
        output.append(tokens[l:l + chunk_size])
        l += step_size
        
    return output