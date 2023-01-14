import time
start = time.process_time()
x =0
y=0
for i in range(1,101):
    x+=(i**2)
    y+=i
y= y**2

print(y-x)
end=time.process_time()
print(f"{end-start}seconds")

