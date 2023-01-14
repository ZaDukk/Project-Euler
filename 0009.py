import time
start = time.process_time()

oneKnums = [i for i in range(1,1001)]

for a in oneKnums:
    for b in oneKnums:
        c = 1000-(a+b)
        if (a**2 + b**2 == c**2):
            print(a*b*c)
            oneKnums=[]
            
end = time.process_time()
print(f"{end-start}seconds")

