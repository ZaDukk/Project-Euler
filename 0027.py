from tools import primesLessThan #tools is a file see the bottom of the repo
from itertools import count
from time import process_time

start=process_time()

primes = set(primesLessThan(7920))
brange = primesLessThan(1000)
arange = [-i for i in brange]
print("primes generated")
largest=0
res=0

for a in arange:
    for b in brange:
        if a+b+1 not in primes:
            continue
        for n in count():
            if ((n**2) +(a*n) +b) not in primes:
                if n >largest:
                    largest=n
                    res=a*b
                break

print(res)

end = process_time()
print(f"{end-start}seconds")
