numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    for y in range(1, (i // 2) + 1):
        if y > 1 and y < (i // 2) + 1 and i % y == 0:
            not_primes.append(i)
            break
        if y >= i // 2:
            primes.append(i)
            break
print(primes)
print(not_primes)