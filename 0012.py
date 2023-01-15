from time import process_time
from sympy import divisors
start = process_time()

n=2
while True:
    t = int(0.5*n*(n+1))
    if len(divisors(t))>500:
        print(t)
        break
    n+=1
end=process_time()
print(f"{end-start}seconds")

    