def fibonacci():
    a = 0
    b = 1

    while True:
        c = a + b
        yield c
        a = b
        b = c

fibonacci_generator = fibonacci()

total = 0
f = 0

while f < 4_000_000:
    f = next(fibonacci_generator)

    if f % 2 == 0:
        total += f

print(total)
