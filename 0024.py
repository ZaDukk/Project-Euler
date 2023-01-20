from time import process_time
start = process_time()

from itertools import permutations
x = list(permutations("0123456789"))
print("".join(x[1000000-1]))


end = process_time()
print(f"{end-start}seconds")