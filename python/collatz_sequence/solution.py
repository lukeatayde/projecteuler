def generate_next_collatz(n):
    """
    INPUT: an integer n > 1
    OUTPUT: the next integer in a collatz sequence following the int n
    """
    if n % 2 == 0:
        return n / 2
    else:
        return 3*n + 1

length = []
for i in range(1, 1000000):
    value = i
    count = 1
    while value != 1:
        value = generate_next_collatz(value)
        count += 1
    length.append(count)

max = max(length)
print(f"Starting number: { length.index(max) + 1 }, Max: { max }")
