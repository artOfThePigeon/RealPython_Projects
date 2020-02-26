# Below are code snippets I used in practicing with dataframes.

import pandas as pd

# the following reads the .csv created in main.py.
df = pd.read_csv('data.csv', index_col=0)

# the following code creates a excel doc from the dataframe.
df.to_excel('data.xlsx')

# the following produces a nan output indicating it is missing.
df.loc['RUS', 'CONT']

# this shows what datatypes panda assigns to the imported values
df.dtypes

# the following specifies my desired data types
dtypes = {'POP': 'float32', 'AREA': 'float32', 'GDP': 'float32'}

# this forces the use of datetimes
df = pd.read_csv('data.csv', index_col=0, dtype=dtypes,
                 parse_dates=['IND_DAY'])
# shows the result.
df.dtypes

df['IND_DAY']
