from time import process_time
start = process_time()

num = 1
longest = 1
for n in range(3, 1000, 2):
    l = 1
    if n%5==0:
        continue
    while (10 ** l) % n != 1:
        l += 1

    if l > longest:
        num=n
        longest = l

print(num)


end=process_time()
print(f"{end-start}seconds")