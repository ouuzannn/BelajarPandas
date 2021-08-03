import pandas as pd
import numpy as np

print(pd.__version__)
print(np.__version__)

row = 5
col = 5

cols = tuple('ABCDE')

df = pd.DataFrame(np.random.randint(1, 10, size=(row,col)), columns=cols)

print(df)

print(df.add_prefix('kolom'))
print(df.add_suffix('_field'))