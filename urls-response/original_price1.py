import os

files = os.listdir(".")

result = "original_price"
exitsfiles = []
for fname in files:
    if fname == 'original_price.py':
        continue

    f = open(fname)
    flag = False 
    for line in f:
        if "<del" in line:
            flag = not flag
            exitsfiles.append(fname)
    if flag:
            exitsfiles.append("")
for f in files:
    if f not in exitsfiles:
        print(f)
