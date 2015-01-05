import collections

words = collections.defaultdict(list)
with open("cikti.txt") as f:
    lines = [l.strip() for l in f if l.strip()]

for word in lines:
    words[word[0]].append(word)

print words
