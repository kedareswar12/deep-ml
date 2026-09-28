def vector_sum(a: list[int|float], b: list[int|float]) -> list[int|float] | int:
    # Return the element-wise sum of vectors 'a' and 'b'.
    # If vectors have different lengths, return -1.
    if len(a) != len(b):
        return -1
    
    result = []
    
    # Loop over indices from 0 to len(a) - 1
    for i in range(len(a)):
        total = a[i] + b[i]
        result.append(total)
        
    return result