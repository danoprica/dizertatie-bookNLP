import pandas as pd

df = pd.read_csv("works/gibson/gibson_uniquesSupersenseLemmas.tsv", delimiter="\t")

df = (df['supersense_category'])

df = df.value_counts()


df.to_csv("works/gibson/gibson_uniquesLemmasPercentages.tsv", sep="\t")