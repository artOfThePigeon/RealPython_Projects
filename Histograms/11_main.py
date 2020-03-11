# bins data based in sensible intervals based on level of support package for hours worked

import numpy as np
import pandas as pd

hours = pd.Series(
    [0, 0, 1, 1, 1, 1, 2, 3, 3, 3, 3, 3, 4, 5, 6, 7, 7, 8, 9, 9, 9, 10, 11, 12]
)

bins = [0, 3, 6, 9, 12, np.inf]
labels =['Basic', 'Plus', 'Pro', 'Premium', 'Enterprise']

groups = pd.cut(hours, bins=bins, labels=labels)

print(groups.value_counts())
