import json
import pandas as pd
author = 'gibson'
work = 'new_rose_hotel'

with open('works/' + author + '/' + work + '/' + work + 'CharactersRegexFix.json') as f:
    data = json.load(f)

#print(len(data))
row1 = [] 
row2 = []
row3 = []
row4 = []
row5 = []
row6 = []

for i in range(len(data)):
    row1.append(data[i]['max_proper_mention'])
for i in range(len(data)):
    row2.append(data[i]['count'])
for i in range(len(data)):
    row3.append(len(data[i]['possList']))
for i in range(len(data)):
    row4.append(len(data[i]['agentList']))
for i in range(len(data)):
    row5.append(len(data[i]['patientList']))        
for i in range(len(data)):
    row6.append(len(data[i]['modList']))

df1 = pd.DataFrame(row1, columns=['Characters'])
df2 = pd.DataFrame(row2, columns = ['occourencesCount'])
df3 = pd.DataFrame(row3, columns = ['possCount'])
df4 = pd.DataFrame(row4, columns = ['agentCount'])
df5 = pd.DataFrame(row5, columns = ['patientCount'])
df6 = pd.DataFrame(row6, columns = ['modCount'])

df = pd.concat([df1,df2,df3,df4,df5,df6], axis = 1, join='inner')
df.to_csv('works/' + author + '/' + work + '/' + work + 'CharactersStats.tsv', sep ='\t')
