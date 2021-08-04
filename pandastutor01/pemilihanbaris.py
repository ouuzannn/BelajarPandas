import pandas as pd
import numpy as np

row = 5
col = 5

cols = tuple('ABCDE')

df = pd.DataFrame(np.random.randint(1, 10, size=(row,col)), columns=cols)

print(df)
print(f'\nhasil dari pencarian kolom A yang bernilai 1 atau 3')
print(df[(df['A'] == 1) | (df['A'] == 3)]) 


print('logika isin(sama seperti or)')
print(df[df['A'].isin([1,3])])

print('logika not(negasi)')
print(df[~df['A'].isin([1,3])])