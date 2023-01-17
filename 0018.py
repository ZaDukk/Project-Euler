from time import process_time
start = process_time()


with open("0018input.txt","r") as f:
    t = [[int(n) for n in line.strip().split(' ')]for line in f.readlines()]


for r in range(len(t)-2,-1,-1):
    for c in range(len(t[r])):
        current=t[r][c]
        t[r][c]= max(current+t[r+1][c],current+t[r+1][c+1])
print(t[0][0])


end=process_time()
print(f"{end-start}seconds")