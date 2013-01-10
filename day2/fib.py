def fib(n):
    if n == 1:
        return 1
    elif n < 1:
        return 0
    return fib(n-1) + fib(n-2)

fiblist = [1, 1]

def better_fib(n):
    if len(fiblist) >= n:
        return fiblist[n-1]
    elif len(fiblist) == (n - 1):
        fiblist.append(fiblist[n-2] + fiblist[n - 3])
        return fiblist[n-1]
    else:
        return better_fib(n - 1) + better_fib(n - 2)
