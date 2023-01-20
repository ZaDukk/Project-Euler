import time

start = time.process_time()
res=1
for i in range(3,1002,2):
    res+=4*(i**2)-6*(i-1)
print(res)
end = time.process_time()

print(f"{end-start}seconds")