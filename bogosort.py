import random

def bogosort(seq):
    while not is_sorted(seq):
        random.shuffle(seq)


def is_sorted(seq):
    for i in range(len(seq) - 1):
        if seq[i] > seq[i + 1]:
            return False
    return True

