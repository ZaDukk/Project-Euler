from time import process_time
start = process_time()
#this problem is the same as 18

with open("0067input.txt","r") as f:
    t = [[int(n) for n in line.strip().split(' ')]for line in f.readlines()]


for r in range(len(t)-2,-1,-1):
    for c in range(len(t[r])):
        current=t[r][c]
        t[r][c]= max(current+t[r+1][c],current+t[r+1][c+1])
print(t[0][0])


end=process_time()
print(f"{end-start}seconds")