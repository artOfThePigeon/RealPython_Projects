# This exercise defines a list and then creates a function to
# group it into bins and count how many times a value appears in
# each bin.
# Then, Counter is used to do the same thing without
# a lot of code. I then test for functional equivalence.

from collections import Counter


a = [0, 1, 1, 1, 0, 2, 3, 7, 7, 23]

# function takes a sequence, and returns a dictionary
def count_elements(seq) -> dict:
    hist = {}
    for i in seq:
        # take the hist dictionary at the i index, and return value or 0
        hist[i] = hist.get(i, 0) + 1
    return hist

# pass in list a, then print the dictionary object
counted = count_elements(a)
print(counted)

# collections module Counter produces similar result
recounted = Counter(a)
print(recounted)

# make sure they are functionally equivalent
print(recounted.items() == counted.items())
