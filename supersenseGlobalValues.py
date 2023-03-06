import pandas as pd

df = pd.read_csv("works/supersenseTemplate.tsv", delimiter="\t")
df1 = pd.read_csv("works/gibson/burning_chrome/burning_chrome.supersense", delimiter="\t")
df2 = pd.read_csv("works/gibson/hinterlands/hinterlands.supersense", delimiter="\t")
df3 = pd.read_csv("works/gibson/johnny_mnemonic/johnny_mnemonic.supersense", delimiter="\t")
df4 = pd.read_csv("works/gibson/neuromancer/neuromancer.supersense", delimiter="\t")
df5 = pd.read_csv("works/gibson/new_rose_hotel/new_rose_hotel.supersense", delimiter="\t")

df1 = (df1['supersense_category'])
df2 = (df2['supersense_category'])
df3 = (df3['supersense_category'])
df4 = (df4['supersense_category'])
df5 = (df5['supersense_category'])


df1 = df1.value_counts()
df2 = df2.value_counts()
df3 = df3.value_counts()
df4 = df4.value_counts()
df5 = df5.value_counts()


df1.loc["noun.process"] = 0
df2.loc["noun.motive"] = 0
df3.loc["noun.motive"] = 0
df3.loc["noun.process"] = 0
df5.loc["noun.motive"] = 0

df = (df1 + df2 + df3 + df4 + df5)

df.to_csv("works/gibson/gibson_supersenseGlobal.tsv", sep="\t")

print (df)






