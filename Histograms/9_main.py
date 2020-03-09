# computes a historgram into a pandas series

import numpy as np
import pandas as pd

data = np.random.choice(np.arange(10), size=10000,
                        p=np.linspace(1, 11, 10) / 60)

s = pd.Series(data)

# normalizes the data, then 'head' prints the top 5 largest
print(s.value_counts(normalize=True).head())
