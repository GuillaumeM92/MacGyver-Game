# Defining our list
squares = list(range(225))


def chunk_it(seq, num):
    """
        Split an array into a number of chunks
        seq: List
        num: length of the sequence
    """
    avg = len(seq) / float(num)
    out = []
    last = 0.0

    while last < len(seq):
        out.append(seq[int(last):int(last + avg)])
        last += avg

    return out


# Getting all 16 items chunks of squares
grid = chunk_it(squares,15)

# Testing behaviour
print(grid)
print(grid[2][12])
