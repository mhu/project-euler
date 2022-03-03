from itertools import permutations

def is_palindrome(num):
    num_str = str(num)
    return num_str == num_str[::-1]


palindromes = []

for x, y in permutations(range(1000), 2):
    if is_palindrome(x * y):
        palindromes.append(x * y)

print(max(palindromes))
