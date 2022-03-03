target = 600851475143

n = 2
prime_factors = []

while target != 1:
    tested_value = target / n
    if tested_value.is_integer():
        prime_factors.append(n)
        target = tested_value
    n += 1

print(max(prime_factors))
