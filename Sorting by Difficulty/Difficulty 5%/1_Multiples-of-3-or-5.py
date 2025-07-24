def sum_of_multiples(limit):
    total = 0
    for number in range(limit):
        if number % 3 == 0 or number % 5 == 0:
            total += number
    return total

print(sum_of_multiples(1000))

#233168