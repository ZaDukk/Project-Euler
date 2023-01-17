from sympy import divisors
import time
start = time.process_time()

def d(n):
    total=0
    for i in divisors(n):
        total+=i
    total-=n
    return total

seen=set()
for a in range(1,10000):
    b=d(a)
    if a not in seen and b not in seen:
        if d(b)==a and a!=b:
            seen.add(a)
            seen.add(b)
    else:
        continue

print(sum(seen))
end = time.process_time()
print(f"{end-start}seconds")
