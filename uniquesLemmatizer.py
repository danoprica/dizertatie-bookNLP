import spacy
import pandas as pd
nlp = spacy.load('en_core_web_lg')
df_uniques = pd.read_csv("works/gibson/gibson_uniquesSupersense.tsv", delimiter="\t")

for i, row in df_uniques.iterrows():
    text = row['text']
    text = nlp(text)
    text = "".join([token.lemma_ for token in text])
    row['text'] = text

df_uniques = df_uniques.drop_duplicates()

df_uniques.to_csv("works/gibson/gibson_uniquesSupersenseLemmas.tsv", sep="\t")




