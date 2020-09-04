
f = open("original_price")
rf = open("wbcs", "w+")

for line in f:
    if None == line or "" == line.strip() or len(line) == 0:
        print("null----------------")
        rf.write("\n")
        continue

    wbcs = line.split("<!-- -->人想买")
    wbc = wbcs[0].split("等<!-- -->")[1]
    print(wbc)
    rf.write(wbc+"\n")
   # if not 2 == len(ops):
   #     print(line)
   #     rf.write(line)
   #     exit(0)
   # else:
   #     op = ops[1].split("</del>")[0].split(">")[1]
   #     print(op)
rf.close()
