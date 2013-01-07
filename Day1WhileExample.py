#find the highest integer factorial less than n using a while loop

def factorialupto(n=10000):
    a = 1
    count = 1
    while a < n:
        count += 1
        a *= count
    return a / count
