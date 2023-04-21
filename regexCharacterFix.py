import json
import re

author = 'lovecraft'
work = 'the_whisperer_in_darkness'

with open('works/' + author + '/' + work + '/' + work + 'Characters.json') as f:
    data = json.load(f)



data = str(data)
data = re.sub("'+[0-9]+'+:", '', data)
data = data[1:-1]
data = "[" + data + "]"
data = re.sub("'", '"', data)


g = open('works/' + author + '/' + work + '/' + work + 'CharactersRegexFix.json', "x")
g.write(data)
g.close()
