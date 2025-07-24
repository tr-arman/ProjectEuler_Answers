import math

def count_divisors(n):
    count = 0
    sqrt_n = int(math.sqrt(n))
    for i in range(1, sqrt_n + 1):
        if n % i == 0:
            count += 2
    if sqrt_n * sqrt_n == n:
        count -= 1
    return count


def first_triangle_with_divisors(limit):
    n = 1
    triangle = 0
    while True:
        triangle += n
        if count_divisors(triangle) > limit:
            return triangle
        n += 1

print(first_triangle_with_divisors(500))

#76576500
#https://projecteuler.net/problem=12
#WITHOUT IMPORT MATH:

def count_divisors(n):
    count = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            count += 2
        i += 1
    if (i - 1) * (i - 1) == n:
        count -= 1
    return count


def first_triangle_with_divisors(limit):
    triangle = 0
    n = 1
    while True:
        triangle += n
        if count_divisors(triangle) > limit:
            return triangle
        n += 1

print(first_triangle_with_divisors(500))