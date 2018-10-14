
def sort(seq):
    a = False
    while not a:
        a = True
        for i in range(len(seq) - 1):
            if seq[i] > seq[i + 1]:
                temp = seq[i + 1]
                seq[i + 1] = seq[i]
                seq[i] = temp
                a = False

