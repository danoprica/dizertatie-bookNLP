import spacy
import pandas as pd
nlp = spacy.load('en_core_web_lg')
df_uniques_dick = pd.read_csv("works/dick/dick_uniquesSupersense.tsv", delimiter="\t")
#for row in df_uniques_dick['text']:
    #text = ''
    #for token in nlp(row):
        #text = text + token
    #print (text)  
        

test = 'thinking known unknown went'
test = nlp(test)
y = " ".join([token.lemma_ for token in test]) 
print(y)

#df_uniques_dick['text'].apply(lambda row: " ".join([w.lemma_ for w in nlp(row)]))

#print(df_uniques_dick)

