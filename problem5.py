def is_divisible(num):
    for divisor in range(20, 0, -1): # reversing the range for speed
        if not (num / divisor).is_integer():
            return False
    return True

n = 2520

while not is_divisible(n):
    n += 1

print(n)
