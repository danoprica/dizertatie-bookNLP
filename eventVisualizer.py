import pandas as pd
import matplotlib.pyplot as plt
import csv

author = 'lovecraft'
work = 'call_of_cthulhu'

df = pd.read_csv("works/" + author + "/" + work + "/" + work + "EventPerSent.tsv", sep='\t', quoting=csv.QUOTE_NONE)

df.plot(x='sentence_ID', y='eventCount')

plt.show()