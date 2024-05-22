import pandas as pd
import os
import glob

# uma função de extract que lê e consolida os json

pasta = 'data'
arquivos_json = glob.glob(os.path.join(pasta, '*json'))
df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
df_total = pd.concat(df_list, ignore_index=True)

print(df_total)

# uma função que transforma

# uma função que da load em csv ou parquet