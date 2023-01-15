from time import process_time
start = process_time()

seen = {}

def collatz(n):
    if n not in seen:
        if n == 1:           
            seen[n]=1
        elif n % 2 == 0:     
            seen[n]=collatz(n // 2) + 1     
        else:
            seen[n]=collatz(3*n + 1) + 1
    return seen[n]


largest = 1
for i in range(1,1000000):
    if collatz(i) > collatz(largest):
        largest = i

print(largest)
end=process_time()
print(f"{end-start}seconds")
