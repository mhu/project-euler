primes = []

def generate_primes():
    n = 2

    while True:
        if is_prime(n):
            yield n
        n += 1

def is_prime(n):
    for prime in primes:
        if n % prime == 0:
            return False
    return True

generator = generate_primes()

while len(primes) < 10001:
    primes.append(next(generator))

print(primes[-1])
