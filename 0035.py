from tools import isPrime
from time import process_time
start = process_time()


res=0
for i in range(2,1000000):
    res+=1
    for j in range(len(str(i))):
        if isPrime(int(str(i)[j:] + str(i)[:j])) == False:
            res-=1
            break
end = process_time()
print(res)
print(f"{end-start}seconds")


