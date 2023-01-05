def fact(n):
    """Calculate n! iteratively."""
    result = 1
    while n > 1:
        result = result*n
        n -= 1
    return result


def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def fib(n):
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        n1 = 1
        n2 = 0
        for f in range(1, n):
            result = n1 + n2
            n2 = n1
            n1 = result
    return result


print(fact(5))
print(fibonacci(5))
print()
for f in range(36):
    print(fib(f))
