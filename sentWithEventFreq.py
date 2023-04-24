import pandas as pd
import csv
author = 'gibson'
work1 = 'burning_chrome'
work2 = 'hinterlands'
work3 = 'johnny_mnemonic'
work4 = 'neuromancer'
work5 = 'new_rose_hotel'

df1 = pd.read_csv("works/" + author + "/" + work1 + "/" + work1 + ".tokens", sep='\t', quoting=csv.QUOTE_NONE)
df2 = pd.read_csv("works/" + author + "/" + work2 + "/" + work2 + ".tokens", sep='\t', quoting=csv.QUOTE_NONE)
df3 = pd.read_csv("works/" + author + "/" + work3 + "/" + work3 + ".tokens", sep='\t', quoting=csv.QUOTE_NONE)
df4 = pd.read_csv("works/" + author + "/" + work4 + "/" + work4 + ".tokens", sep='\t', quoting=csv.QUOTE_NONE)
df5 = pd.read_csv("works/" + author + "/" + work5 + "/" + work5 + ".tokens", sep='\t', quoting=csv.QUOTE_NONE)

rows1 = []
rows2 = []
rows3 = []

rows1.append(work1)
rows1.append(work2)
rows1.append(work3)
rows1.append(work4)
rows1.append(work5)




rows3.append(df1.iloc[-1][1])
rows3.append(df2.iloc[-1][1])
rows3.append(df3.iloc[-1][1])
rows3.append(df4.iloc[-1][1])
rows3.append(df5.iloc[-1][1])