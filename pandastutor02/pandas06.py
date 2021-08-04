import pandas as pd
import numpy as np

row = 5
col = 5
cols = tuple('ABCDE')
df = pd.DataFrame(np.random.randint(1, 10, size=(row,col)),columns=cols)

print(df)

#cara mengubah nama kolom 
df = df.rename(columns={'C':'Hobi','A':'contoh'})
print(f'hasil perubahan nama kolom :\n{df}')