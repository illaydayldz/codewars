def factorial(number):
    total = 1
    i = 1
    while i <= number:
        total *= i
        i += 1

    return total

print(factorial(5))