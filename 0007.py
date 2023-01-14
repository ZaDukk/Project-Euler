import math
import time
start = time.process_time()


def isPrime(n):
    if n ==2:
        return True
    if n==3:
        return True
    
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
        
    return True

primes=0
res=1
while primes!=10001:
    res+=1
    if isPrime(res):
        primes+=1
    
    #print(f"n:{res},primes:{primes}")
print(res)




end = time.process_time()
print(f"{end-start}seconds")


