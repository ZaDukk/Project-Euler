from time import process_time
start = process_time()

n = [1,1]

while len(str(n[len(n)-1]))!=1000:
    n.append(n[len(n)-1]+n[len(n)-2])
print(len( n))



end=process_time()
print(f"{end-start}seconds")