import pandas as pd
import csv

author = 'lovecraft'
work = 'call_of_cthulhu'

df = pd.read_csv("works/" + author + "/" + work + "/" + work + ".tokens", sep='\t', quoting=csv.QUOTE_NONE)

eventCount = 0

eventList = []

initialID = 0

for i in range(len(df)):
    if(df.iloc[i]['sentence_ID'] == initialID):
        if (df.iloc[i]['event']) == 'EVENT':
            eventCount = eventCount + 1

    else:
        eventList.append(eventCount) 
        eventCount = 0
        initialID = initialID + 1

#print (eventList)               

id_list = df['sentence_ID'].values.tolist()
id_list = list(dict.fromkeys(id_list))


df_final1 = pd.DataFrame(id_list, columns = ['sentence_ID'])
df_final2 = pd.DataFrame(eventList, columns = ['eventCount'])
df_final = pd.concat([df_final1,df_final2], axis = 1, join='inner')
df_final.to_csv('works/' + author + '/' + work + '/' + work + 'EventPerSent.tsv', sep ='\t')