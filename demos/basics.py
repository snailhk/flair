# -*- coding: utf-8 -*-

from flair.data import Sentence
from flair.data import Label

sentence = Sentence("The grass is green .")

print(sentence)

print(sentence.get_token(4))
print(sentence[3])

for token in sentence:
    print(token)


ss = Sentence("The grass is green.", use_tokenizer=True)
print(ss)

ss[3].add_tag("ner", "color")
print(ss.to_tagged_string())

tag: Label = ss[3].get_tag("ner")


sens = Sentence("France is the current world cup winner.")
sens.add_label("sports")
sentence.add_labels(["sports", "world cup"])
sentens = Sentence("France is th ccurrent world cup winner.", labels=["sports", "world cup"])
print(sentens)

for label in sentens.labels:
    print(label)


