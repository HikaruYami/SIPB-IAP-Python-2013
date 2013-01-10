total = 0
for a in [2, 3, 5, 6, 7]:
    if (a % 3 == 0):
        total += a
    elif (a % 5 == 0):
        total += a
    else:
        pass
print total

def sumvars(a=3, b=5, c=1000):
    total = 0
    for n in range(c):
        if (n % a == 0 or n % b == 0):
            total += n
    return total
