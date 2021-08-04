import pandas as pd
import numpy as np

row = 5
col = 5
cols = tuple('ABCDE')

df = pd.DataFrame(np.random.randint(1, 10, size=(row,col)),columns=cols)
print(df)
print('membalik urutan kolom ')
print(df.loc[:, ::-1])

print('membalik urutan baris ')
print(df.loc[::-1, :])

print('\nmembalik urutna baris tetapi indexnya di generalisir lagi')
print(df.loc[::-1].reset_index(drop=True))