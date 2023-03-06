import json
import re
with open('works/dick/impostor/impostorCharactersRegexFix.json') as f:
    data = json.load(f)

for i in range(len(data)):
    print(data[i]['max_proper_mention'])

#print(len(data))