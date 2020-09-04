
f = open("original_price")
rf = open("ops", "w+")

for line in f:
    if None == line or "" == line.strip() or len(line) == 0:
        print("null----------------")
        rf.write("\n")
        continue

    ops = line.split("<del>")
    op = ops[1].split("</del>")[0].split(">")[1]
    print(op)
    rf.write(op+"\n")
   # if not 2 == len(ops):
   #     print(line)
   #     rf.write(line)
   #     exit(0)
   # else:
   #     op = ops[1].split("</del>")[0].split(">")[1]
   #     print(op)
rf.close()
