numbers = range(1000)

solution = sum(filter(lambda n: n % 3 == 0 or n % 5 == 0, numbers))

print(solution)
