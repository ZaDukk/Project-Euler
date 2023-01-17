import time
start = time.process_time()

with open("0022input.txt","r")as f:
    x=f.readlines()

x=x[0]
x= x.split(",")
names = [i.strip("\"\'") for i in x]
names.sort()

def getScore(s):
    total=0

    for i in s:
        total+=ord(i)-64
    return total
res=0
for i,name in enumerate(names):
    res+=(getScore(name)*(i+1))

print(res)

end = time.process_time()
print(f"{end-start}seconds")