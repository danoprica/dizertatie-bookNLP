import pandas as pd

author = 'lovecraft'
work1 = 'at_the_mountains_of_madness'
work2 = 'call_of_cthulhu'
work3 = 'the_colour_out_of_space'
work4 = 'the_shadow_over_innsmouth'
work5 = 'the_whisperer_in_darkness'

df1 = pd.read_csv("works/" + author + "/" + work1 + "/" + work1 + "CharactersStats.tsv", sep='\t')
df2 = pd.read_csv("works/" + author + "/" + work2 + "/" + work2 + "CharactersStats.tsv", sep='\t')
df3 = pd.read_csv("works/" + author + "/" + work3 + "/" + work3 + "CharactersStats.tsv", sep='\t')
df4 = pd.read_csv("works/" + author + "/" + work4 + "/" + work4 + "CharactersStats.tsv", sep='\t')
df5 = pd.read_csv("works/" + author + "/" + work5 + "/" + work5 + "CharactersStats.tsv", sep='\t')

totalOcurences = df1['occourencesCount'].sum() + df2['occourencesCount'].sum() + df3['occourencesCount'].sum() + df4['occourencesCount'].sum() + df5['occourencesCount'].sum()
print (totalOcurences)