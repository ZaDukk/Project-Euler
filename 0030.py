from time import process_time
start = process_time()

res = 0
for n in range(1, 1000000): #arbitrary large number that works
    x = sum([int(i) ** 5 for i in str(n)])
    if x == n:
        res += n
# i genuinely have no idea why there is an off by one error
print(res - 1)

end=process_time()
print(f"{end-start}seconds")