import pandas as pd
import matplotlib.pyplot as plt
import csv

author = 'dick'
work = 'electric_ant'

df = pd.read_csv("works/" + author + "/" + work + "/" + work + ".tokens", sep='\t', quoting=csv.QUOTE_NONE)

x = 0
for i in df['sentence_ID']:
    x = x + 1

print(x)

#df.plot.scatter(x='sentence_ID', y ='event')
#plt.show()