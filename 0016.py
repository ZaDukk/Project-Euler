from time import process_time
start = process_time()

n=str(2**1000)
res=0
for i in n:
    res+=int(i)
print(res)

end=process_time()
print(f"{end-start}seconds")