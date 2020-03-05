#presents data in a histogram using a pandas series

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

means = 10, 20
stdevs = 4, 2

dist = pd.DataFrame(
    np.random.normal(loc=means, scale=stdevs, size=(1000,2))
    columns=['a','b']
)

print(dist.agg(['min','max','mean','std']))
