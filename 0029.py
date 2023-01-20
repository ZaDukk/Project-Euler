from time import process_time
start =process_time()

nums = set()
for a in range(2,101):
    for b in range(2,101):
        nums.add(a**b)
print(len(nums))

end = process_time()
print(f"{end-start}seconds")