#determine if a number is prime or composite (inefficiently, but completely)

def isprime(n):
    a = 2
    if (n < 2):
        return False
    while a <= n ** .5:
        if n % a == 0:
            return False
        a += a%2 + 1
    return True
