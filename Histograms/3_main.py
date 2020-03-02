# The following uses numpy to bin data between defined edges, then map it to frequencies of how many times each range occurs.

import numpy as np

np.random.seed(444)
np.set_printoptions(precision=3)

d = np.random.laplace(loc=15, scale=3, size=500)

hist, bin_edges = np.histogram(d)
print("The hist piece below is the frequency counts that would appear for each bin. In this case, there were 13 occurences, then 23, etc. \n", hist)
print()
print("The bin_edges below show the cutoffs that separate each group of data points. The number 5.874 would be excluded from the first bin, and included in the second. \n",bin_edges)
