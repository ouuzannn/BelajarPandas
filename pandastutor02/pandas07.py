import pandas as pd
import numpy as np

df = pd.util.testing.makeMissingDataframe().reset_index()
df.head()
# print(df.head())

df = df.rename(columns={'index':'z'})
print(df.head())


df_backup = df.copy(deep=True)

# menghapus (Drop) setiap kolom yang mengandung missing values
df = df.dropna(axis = 'columns')
print(df.head())

# menghapus (Drop) setiap baris yang mengandung missing values
df = df_backup.copy(deep=True)
df = df.dropna(axis = 'rows')
print(df.head())

# persentase missing values untuk tiap kolom 
df = df_backup.copy(deep=True)
df = df.isna().mean()
print(f'persentase missing values untuk tiap kolom {df.head()}')

#menghapus (drop) setiap kolom yang mengandung missing values berdasarkan threshold

treshold = len(df) * 0.9
df = df.dropna(thresh=treshold, axis='columns')
print(f'hasil tabel dengan batas persentasi di setiap kolom yang mengandung missing values berdasarkan threshold \n{df.head()}')