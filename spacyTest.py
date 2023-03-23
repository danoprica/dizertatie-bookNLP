import spacy
import pandas as pd
nlp = spacy.load('en_core_web_lg')
df_uniques_dick = pd.read_csv("works/dick/dick_uniquesSupersense.tsv", delimiter="\t")

for i, row in df_uniques_dick.iterrows():
    #text = nlp(row[i, 'text'])
    
    #df_uniques_dick.at[i, 'text'] = text
    text = row['text']
    text = nlp(text)
    text = "".join([token.lemma_ for token in text])
    row['text'] = text

df_uniques_dick = df_uniques_dick.drop_duplicates()
print(df_uniques_dick)

#for row in df_uniques_dick['text']:
    #text = nlp(row)
    #text = " ".join([token.lemma_ for token in text])  
    #print (text)


#print (df_uniques_dick)        

#test = 'thinking known unknown went'
#test = nlp(test)
#y = " ".join([token.lemma_ for token in test]) 
#print(y)

#df_uniques_dick['text'].apply(lambda row: " ".join([w.lemma_ for w in nlp(row)]))

#print(df_uniques_dick)

