import pandas as pd
import numpy as np


# print(pd.__version__)
data = {'col1':['1','2','3','teks'],'col2':['1','2','3','4']}

df = pd.DataFrame(data)
print(df)

print(df.dtypes)

print('\nkonversi tipe data yaitu data di col2 menjadi integer')
df_x = df.astype({'col2':'int'})
print('Perubahan jenis data :')
print(df_x.dtypes)

#konversi ke numerik 
# maksud coerce -> apabila ada data yng tidak bisa dikonversi ke numerik maka dat atersebut akan menjadi NaN(undifined)
print(df.apply(pd.to_numeric, errors='coerce'))
