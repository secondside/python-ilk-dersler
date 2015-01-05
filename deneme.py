d = {}
a = open("engin.txt", "w")

with open("cikti.txt") as f:
    for line in f:
       (key, val) = line.split()
       d[(key)] = val
       a.write(line)

i = d[(val)]

print dict.fromkeys("a"[int(i)])
