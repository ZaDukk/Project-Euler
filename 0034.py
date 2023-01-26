from time import process_time
from math import factorial

start = process_time()

res=0
for i in range(3,50000):
    if i == sum(factorial(int(n)) for n in str(i)):
        res+=i
print(res)

end = process_time()
print(f"{end-start}seconds")