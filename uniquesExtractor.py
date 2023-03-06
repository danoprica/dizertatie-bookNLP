import pandas as pd

df1 = pd.read_csv("works/dick/impostor/impostor.supersense", delimiter="\t")
df2 = pd.read_csv("works/dick/electric_ant/electric_ant.supersense", delimiter="\t")
df3 = pd.read_csv("works/dick/faith_of_our_fathers/faith_of_our_fathers.supersense", delimiter="\t")
df4 = pd.read_csv("works/dick/impostor/impostor.supersense", delimiter="\t")
df5 = pd.read_csv("works/dick/minority_report/minority_report.supersense", delimiter="\t")

df6 = pd.read_csv("works/gibson/burning_chrome/burning_chrome.supersense", delimiter="\t")
df7 = pd.read_csv("works/gibson/hinterlands/hinterlands.supersense", delimiter="\t")
df8 = pd.read_csv("works/gibson/johnny_mnemonic/johnny_mnemonic.supersense", delimiter="\t")
df9 = pd.read_csv("works/gibson/neuromancer/neuromancer.supersense", delimiter="\t")
df10 = pd.read_csv("works/gibson/new_rose_hotel/new_rose_hotel.supersense", delimiter="\t")

df11 = pd.read_csv("works/lovecraft/call_of_cthulhu/call_of_cthulhu.supersense", delimiter="\t")
df12 = pd.read_csv("works/lovecraft/at_the_mountains_of_madness/at_the_mountains_of_madness.supersense", delimiter="\t")
df13 = pd.read_csv("works/lovecraft/the_colour_out_of_space/the_colour_out_of_space.supersense", delimiter="\t")
df14 = pd.read_csv("works/lovecraft/the_shadow_over_innsmouth/the_shadow_over_innsmouth.supersense", delimiter="\t")
df15 = pd.read_csv("works/lovecraft/the_whisperer_in_darkness/the_whisperer_in_darkness.supersense", delimiter="\t")

df_dick = pd.concat([df1, df2, df3, df4, df5])
df_gibson = pd.concat([df6, df7, df8, df9, df10])
df_lovecraft = pd.concat([df11, df12, df13, df14, df15])

#df_not_dick = pd.concat([df_gibson, df_lovecraft])
#df_not_lovecraft = pd.concat([df_gibson, df_dick])
#df_not_gibson = pd.concat([df_lovecraft, df_dick])


#df_merged = df_lovecraft.merge(df_not_lovecraft, how="left", left_on=["supersense_category", "text"], right_on=["supersense_category", "text"], indicator=True)
#df = df_merged.query("_merge == 'left_only'")[["supersense_category", "text"]]
#df.to_csv("works/lovecraft/lovecraft_uniquesSupersense.tsv", sep="\t")

df_uniques_dick = pd.read_csv("works/dick/dick_uniquesSupersense.tsv", delimiter="\t")
df_uniques_lovecraft = pd.read_csv("works/lovecraft/lovecraft_uniquesSupersense.tsv", delimiter="\t")
df_uniques_gibson = pd.read_csv("works/gibson/gibson_uniquesSupersense.tsv", delimiter="\t")


print(round(len(df_uniques_dick)/len(df_dick)*100, 2))
print(round(len(df_uniques_lovecraft)/len(df_lovecraft)*100, 2))
print(round(len(df_uniques_gibson)/len(df_gibson)*100, 2))

