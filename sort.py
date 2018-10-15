
def sort(seq):
    """
    Sorts a given list.
    """
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(len(seq) - 1):
            if seq[i] > seq[i + 1]:
                temp = seq[i + 1]
                seq[i + 1] = seq[i]
                seq[i] = temp
                is_sorted = False

def qsort(seq):
    if len(seq) <= 1:
        return seq

