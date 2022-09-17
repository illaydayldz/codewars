def factorial(n):
    total = 1
    i = 1
    while i <= n:
        total *= i
        i += 1

    return total

print(factorial(5))