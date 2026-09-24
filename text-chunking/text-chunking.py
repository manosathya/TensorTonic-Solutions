def text_chunking(tokens: list, chunk_size: int, overlap: int) -> list:
    """
    Returns fixed-size token chunks with the requested overlap.
    """
    step_size = chunk_size - overlap

    start = 0
    output = []
    
    while start < len(tokens) - overlap:
        output.append(tokens[start:start + chunk_size])
        start += step_size
        
    return output