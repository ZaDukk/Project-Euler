from time import process_time

start = process_time()

def isPandigital(x,y):
    testSet = set("123456789")
    if len(str(x))+len(str(y))+len(str(x*y)) == 9:
        if set(str(x) + str(y) + str(x*y)) == testSet:
            return True
    return False

res = set()

for i in range(1,10):
    for j in range(1000,10000):
        if isPandigital(i,j):
            res.add(i*j)
for i in range(10,100):
    for j in range(100,1000):
        if isPandigital(i,j):
            res.add(i*j)

print(sum(res))


end = process_time()
print(f"{end-start}seconds")