import time
start = time.process_time()

def factorial(n):
    if n ==1:
        return 1
    return n*factorial(n-1)
x=str(factorial(100))
res=0
for i in x:
    res+=int(i)
print(res)

end = time.process_time()
print(f"{end-start}seconds")