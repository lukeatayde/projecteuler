import math

values = list(str(int(math.pow(2,1000))))
print values
sum = sum([int(x) for x in values])
print(sum)
