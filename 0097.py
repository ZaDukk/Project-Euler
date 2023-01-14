res = 2
divisor = 10**10

for i in range (7830456):
    res*=2
    res%=divisor

res = ((res*28433) %divisor)+1
print(res)
