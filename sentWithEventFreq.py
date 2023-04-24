import pandas as pd
import csv
author = 'lovecraft'
work1 = 'at_the_mountains_of_madness'
work2 = 'call_of_cthulhu'
work3 = 'the_colour_out_of_space'
work4 = 'the_shadow_over_innsmouth'
work5 = 'the_whisperer_in_darkness'

df1 = pd.read_csv("works/" + author + "/" + work1 + "/" + work1 + ".tokens", sep='\t', quoting=csv.QUOTE_NONE)
df2 = pd.read_csv("works/" + author + "/" + work2 + "/" + work2 + ".tokens", sep='\t', quoting=csv.QUOTE_NONE)
df3 = pd.read_csv("works/" + author + "/" + work3 + "/" + work3 + ".tokens", sep='\t', quoting=csv.QUOTE_NONE)
df4 = pd.read_csv("works/" + author + "/" + work4 + "/" + work4 + ".tokens", sep='\t', quoting=csv.QUOTE_NONE)
df5 = pd.read_csv("works/" + author + "/" + work5 + "/" + work5 + ".tokens", sep='\t', quoting=csv.QUOTE_NONE)

sen_ID1 = []
sen_ID2 = []
sen_ID3 = []
sen_ID4 = []
sen_ID5 = []

rows1 = []
rows2 = []
rows3 = []

rows1.append(work1)
rows1.append(work2)
rows1.append(work3)
rows1.append(work4)
rows1.append(work5)

for i in range(len(df1)):
    if (df1.iloc[i]['event'] == 'EVENT'):
        sen_ID1.append(df1.iloc[i]['sentence_ID']) 

sen_ID1 = list(dict.fromkeys(sen_ID1))
sen_ID1 = len(sen_ID1)


for i in range(len(df2)):
    if (df2.iloc[i]['event'] == 'EVENT'):
        sen_ID2.append(df2.iloc[i]['sentence_ID']) 

sen_ID2 = list(dict.fromkeys(sen_ID2))
sen_ID2 = len(sen_ID2)


for i in range(len(df3)):
    if (df3.iloc[i]['event'] == 'EVENT'):
        sen_ID3.append(df3.iloc[i]['sentence_ID']) 

sen_ID3 = list(dict.fromkeys(sen_ID3))
sen_ID3 = len(sen_ID3)


for i in range(len(df4)):
    if (df4.iloc[i]['event'] == 'EVENT'):
        sen_ID4.append(df4.iloc[i]['sentence_ID']) 

sen_ID4 = list(dict.fromkeys(sen_ID4))
sen_ID4 = len(sen_ID4)


for i in range(len(df5)):
    if (df5.iloc[i]['event'] == 'EVENT'):
        sen_ID5.append(df5.iloc[i]['sentence_ID']) 

sen_ID5 = list(dict.fromkeys(sen_ID5))
sen_ID5 = len(sen_ID5)


rows2.append(sen_ID1)
rows2.append(sen_ID2)
rows2.append(sen_ID3)
rows2.append(sen_ID4)
rows2.append(sen_ID5)


rows3.append(df1.iloc[-1][1])
rows3.append(df2.iloc[-1][1])
rows3.append(df3.iloc[-1][1])
rows3.append(df4.iloc[-1][1])
rows3.append(df5.iloc[-1][1])

df_final1 = pd.DataFrame(rows1, columns =['Work'])
df_final2 = pd.DataFrame(rows2, columns =['No. sentEvent'])
df_final3 = pd.DataFrame(rows3, columns =['No. sentences'])
df_final = pd.concat([df_final1,df_final2,df_final3], axis = 1, join='inner')
df_final.to_csv('works/' + author + '/' + author + 'SentEventStats.tsv', sep ='\t')