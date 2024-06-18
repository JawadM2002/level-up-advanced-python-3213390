from itertools import tee, zip_longest, chain

def pairwise_offset(seq, fillvalue='*', offset=0):
    it1, it2 = tee(seq, 2)
    return zip_longest(it1, chain(fillvalue * offset, it2), fillvalue=fillvalue)
