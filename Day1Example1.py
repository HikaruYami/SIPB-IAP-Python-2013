total = 0
for a in range(1000):
    if (a % 3 == 0 or a % 5 == 0):
        total += a
print total

def sumvars(a=3, b=5, c=1000):
    total = 0
    for n in range(c):
        if (n % a == 0 or n % b == 0):
            total += n
    return total
