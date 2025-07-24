def find_pythagorean_triplet(total_sum):
    for a in range(1, total_sum):
        for b in range(a + 1, total_sum - a):
            c = total_sum - a - b
            if a * a + b * b == c * c:
                return a * b * c

print(find_pythagorean_triplet(1000))

#bruteforced:

def brute_force_pythagorean_triplet():
    for a in range(1, 1000):
        for b in range(a + 1, 1000):
            c = 1000 - a - b
            if c > b and a**2 + b**2 == c**2:
                print(f"Triplet found: a={a}, b={b}, c={c}")
                return a * b * c

print("Product abc:", brute_force_pythagorean_triplet())

#Triplet found: a=200, b=375, c=425
#Product abc: 31875000