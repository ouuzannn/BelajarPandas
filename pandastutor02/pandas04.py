import pandas as pd
import numpy as np

row = 5
col = 2
cols = ['bil_pecahan','bil_bulat']

df = pd.DataFrame(np.random.randint(1, 20, size=(row,col)),columns=cols)

#untuk membuat date time
df['bil_pecahan'] = df['bil_pecahan'].astype('float')

df.index = pd.util.testing.makeDateIndex(row, freq='H')
df = df.reset_index()

df['teks'] = list('ABCDE')

print(df)


print('/nmemilih data yang numerik saja')
print(df.select_dtypes(include='number'))

print('/nmemilih data yang numerik saja (float)')
print(df.select_dtypes(include='float'))

print('/nmemilih data yang numerik saja(int)')
print(df.select_dtypes(include='int'))

print('/nmemilih data yang numerik atau objek saja')
print(df.select_dtypes(include=['number','object']))