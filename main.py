import pandas as pd

df = pd.read_csv('keywords (1).csv', sep=';')
df.info()
print(len(df))
for i in range(len(df)):
    df.loc[i, "'Keyword'"] = " ".join([s.replace('[', '').replace(']', '')
                                       for s in df.loc[i, "'Keyword'"].split() if not s.startswith('-')])
print(df["'Keyword'"].head(5))