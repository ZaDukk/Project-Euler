from time import process_time
from fractions import Fraction

start = process_time()

res=1



for i in range(10,100):
    for j in range(i+10,100):
        intersection = list(set(str(i)) & set(str(j)))
        if len(intersection)!=0 and "0" not in intersection:
            intersection = intersection[0]
            newNumerator = list(str(i))
            newDenominator = list(str(j))
            if newNumerator == newDenominator:
                continue
            newNumerator.remove(intersection)
            newDenominator.remove(intersection)
            if "0" in newNumerator or "0" in newDenominator:
                continue
            if Fraction(int(newNumerator[0]), int(newDenominator[0])) == Fraction(i, j):
                res*=Fraction(i,j)

print(res.denominator)




end = process_time()
print(f"{end-start}seconds")
