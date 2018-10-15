
def sort(seq):
    """
    Returns a sorted version of seq
    """
    a = False
    while not a:
        a = True
        for i in range(len(seq) - 1):
            if seq[i] > seq[i + 1]:
                temp = seq[i + 1]
                seq[i + 1] = seq[i]
                seq[i] = temp
                a = False
    return seq

def qsort(seq):
    if len(seq) <= 1:
        return seq

