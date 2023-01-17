ones = {"0":0,"1":3,"2":3,"3":5,"4":4,"5":4,"6":3,"7":7,"8":5,"9":4}
tens = {"2":6,"3":6,"4":6,"5":5,"6":5,"7":7,"8":6,"9":6}
hundreds= {"1":13,"2":13,"3":15,"4":14,"5":14,"6":13,"7":17,"8":15,"9":14}

weirdCases = {"10":3,"11":len("eleven"), "12":len("twelve"),"13":len("thirteen"),
              "14":len("fourteen"),"15":len("fifteen"), "16":len("sixteen"),"17":len("seventeen"),
              "18":len("eighteen"),"19":len("nineteen")}

res=0
for i in range(1,1000):
    total=0
    if i%100 ==0:
        total-=3
    n = str(i)
    if len(n)==3:
        total+=hundreds[n[0]]
    if len(n)>=2:
        if len(n) ==2:
            z=0
        else:
            z=1
        if n[z] not in ["1", "0"]:
            total += tens[n[z]]
        elif n[z] == "1":
            if len(n)==3:
                n = n[1]+n[2]
            total+=weirdCases[n]
            res+=total
            continue

    total+=ones[n[len(n)-1]]
    res+=total

print(res+11)


