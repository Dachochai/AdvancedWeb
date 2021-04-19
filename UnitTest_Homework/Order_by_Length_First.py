def make_grlex(lst):
    return sorted(lst, key=lambda w: (len(w), w))