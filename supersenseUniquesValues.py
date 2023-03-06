import pandas as pd

df1 = pd.read_csv("works/dick/dick_uniquesSupersense.tsv", delimiter="\t")
df2 = pd.read_csv("works/lovecraft/lovecraft_uniquesSupersense.tsv", delimiter="\t")
df3 = pd.read_csv("works/gibson/gibson_uniquesSupersense.tsv", delimiter="\t")

df1 = (df1['supersense_category'])
df2 = (df2['supersense_category'])
df3 = (df3['supersense_category'])

df1 = df1.value_counts()
df2 = df2.value_counts()
df3 = df3.value_counts()

df1.to_csv("works/dick/dick_supersenseUniquesGlobal.tsv", sep="\t")
df2.to_csv("works/lovecraft/lovecraft_supersenseUniquesGlobal.tsv", sep="\t")
df3.to_csv("works/gibson/gibson_supersenseUniquesGlobal.tsv", sep="\t")

#print(df1)