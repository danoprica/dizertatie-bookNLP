import pandas as pd
import csv
author = 'dick'
work1 = 'do_androids_dream_of_electric_sheep'
work2 = 'electric_ant'
work3 = 'faith_of_our_fathers'
work4 = 'impostor'
work5 = 'minority_report'

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

rows2.append(df1['event'].value_counts()['EVENT'])
rows2.append(df2['event'].value_counts()['EVENT'])
rows2.append(df3['event'].value_counts()['EVENT'])
rows2.append(df4['event'].value_counts()['EVENT'])
rows2.append(df5['event'].value_counts()['EVENT'])

rows3.append(df1.iloc[-1][1])
rows3.append(df2.iloc[-1][1])
rows3.append(df3.iloc[-1][1])
rows3.append(df4.iloc[-1][1])
rows3.append(df5.iloc[-1][1])



df_final1 = pd.DataFrame(rows1, columns =['Work'])
df_final2 = pd.DataFrame(rows2, columns =['No. events'])
df_final3 = pd.DataFrame(rows3, columns =['No. sentences'])
df_final = pd.concat([df_final1,df_final2,df_final3], axis = 1, join='inner')
#df_final.to_csv('works/' + author + '/' + author + 'EventStats.tsv', sep ='\t')
print (df_final)
