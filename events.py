import pandas as pd
df = pd.read_csv("chtulu/chtulu.tokens", delimiter="\t")
events = df[~df['event'].isnull()]
real_events = events.loc[df["event"] == "EVENT"]
event_words = set(real_events.word.tolist())
event_lemmas = list(set(real_events.lemma.tolist()))
event_lemmas.sort()
final_lemmas = []
for lemma in event_lemmas:
    lemma = lemma.lower()
    if lemma not in final_lemmas:
        final_lemmas.append(lemma)
        
sentences = real_events.sentence_ID.tolist()
events = real_events.word.tolist()

def grab_event_sentences(file):
    df = pd.read_csv(file, delimiter="\t")
    real_events = df.loc[df["event"] == "EVENT"]
    sentences = real_events.sentence_ID.tolist()
    event_words = real_events.word.tolist()
    event_lemmas = real_events.lemma.tolist()
    final_sentences = []
    x=0
    for sentence in sentences:
        result = df[df["sentence_ID"] == int(sentence)]
        words = result.word.tolist()
        resentence = " ".join(words)
        final_sentences.append({"event_word": event_words[x],
                                "event_lemma": event_lemmas[x],
                                "sentence": resentence
                                   
                               })
        x=x+1
    return final_sentences
    
    
event_data = grab_event_sentences("chtulu/chtulu.tokens")
new_df = pd.DataFrame(event_data)
new_df.to_csv("chtulu/chtulu.events", index=False)