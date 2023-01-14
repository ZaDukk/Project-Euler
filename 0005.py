import time

start = time.process_time()
currentDivisor =20
res=2520

while currentDivisor>10:
    if res%currentDivisor ==0:
        currentDivisor-=1
    else:
        res+=2520
        currentDivisor=20



print(res)
end = time.process_time()
print(f"{end-start}seconds")