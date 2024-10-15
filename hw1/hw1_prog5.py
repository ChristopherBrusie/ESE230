import math

approx = 0

terms = int(input("how many terms? "))

for i in range(terms):
    approx = approx + 1/math.factorial(i)
print(approx)