##ATTEMPT ONE, WRONG

# def is_triangle(n):
#     x = 8 * n + 1
#     root = int(x ** 0.5)
#     return root * root == x

# def find_nth_triangle_in_sequence(target_count):
#     sequence = [3]
#     triangle_count = 1 if is_triangle(3) else 0

#     n = 0
#     while triangle_count < target_count:
#         current = sequence[-1]
#         if is_triangle(current):
#             next_val = current + 1
#             triangle_count += 1
#         else:
#             next_val = 2 * sequence[-1] - sequence[-2] + 1
#         sequence.append(next_val)
#         n += 1

#     return n

# print(find_nth_triangle_in_sequence(70))

#40744
#https://projecteuler.net/problem=955

##ATTEMPT TWO:

# def is_triangle(n):
#     x = 8 * n + 1
#     s = int(x ** 0.5)
#     return s * s == x

# def find_nth_triangle_in_sequence(target_triangle_index):
#     a = [3]
#     triangle_count = 0
#     index = 0

#     if is_triangle(a[0]):
#         triangle_count += 1

#     while triangle_count < target_triangle_index:
#         if is_triangle(a[-1]):
#             next_val = a[-1] + 1
#             triangle_count += 1
#         else:
#             next_val = 2 * a[-1] - a[-2] + 1
#         a.append(next_val)
#         index += 1

#     return index

# print(find_nth_triangle_in_sequence(70))

#28586
#ATTEMPT THREE:

def is_triangle(n):
    x = 8 * n + 1
    s = int(x ** 0.5)
    return s * s == x

def find_index_of_nth_triangle_in_sequence(target_triangle_count):
    a = [3]
    triangle_count = 1 if is_triangle(3) else 0
    n = 0

    while triangle_count < target_triangle_count:
        if is_triangle(a[-1]):
            next_value = a[-1] + 1
            triangle_count += 1
        else:
            next_value = 2 * a[-1] - a[-2] + 1
        a.append(next_value)
        n += 1

    return n

print(find_index_of_nth_triangle_in_sequence(70))
