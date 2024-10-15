def truncate(num, decimals):
    factor = 10**decimals
    return int(num*factor)/factor

pi = 3.14159
print(truncate(pi, 4))