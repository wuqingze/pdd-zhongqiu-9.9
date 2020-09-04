import os

path = "./data/"
files = os.listdir(path)

result = "original_price"
rf = open(result, "w+")

for fname in files:
    if fname == 'original_price.py':
        continue

    f = open(path+fname)
    flag = True 
    for line in f:
        if "<del" in line:
            flag = not flag 
            rf.write(line)
            print(fname, line)
            break
    if flag:
        rf.write("\n")

rf.close()
            

