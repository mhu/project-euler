sum_of_squares = 0

for n in range(1, 101):
    sum_of_squares += n**2

square_of_sum = sum(range(1, 101)) ** 2

print(square_of_sum - sum_of_squares)
