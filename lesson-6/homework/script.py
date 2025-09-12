def insert_underscores(txt):
    vowels = 'aeiouAEIOU'
    result = ''
    count = 0
    i = 0
    while i < len(txt):
        result += txt[i]
        count += 1
        if count == 3:
            if i+1 < len(txt) and (txt[i] in vowels or (i+1 < len(txt) and txt[i+1] == '_')):
                i += 1
                result += txt[i]
            if i+1 < len(txt): 
                result += '_'
            count = 0
        i += 1
    return result

# Мисоллар:
print(insert_underscores("hello"))
print(insert_underscores("assalom"))
print(insert_underscores("abcabcabcdeabcdefabcdefg"))
n = int(input("n сонни киритинг: "))
for i in range(n):
    print(i**2)
  i = 1
while i <= 10:
    print(i)
    i += 1
  for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=' ')
    print()
    n = int(input("Сон киритинг: "))
total = 0
for i in range(1, n+1):
    total += i
print("Йиғин:", total)
n = int(input("Сон киритинг: "))
for i in range(1, 11):
    print(n * i)
  numbers = [12, 75, 150, 180, 145, 525, 50]
for n in numbers:
    if 75 <= n <= 150:
        print(n)
      n = int(input("Сон киритинг: "))
print("Рақамлар сони:", len(str(n)))
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=' ')
    print()
list1 = [10, 20, 30, 40, 50]
for i in reversed(list1):
    print(i)
for i in range(-10, 0):
    print(i)
for i in range(5):
    print(i)
print("Done!")
for num in range(25, 51):
    if all(num % i != 0 for i in range(2, int(num**0.5)+1)):
        print(num)
a, b = 0, 1
for _ in range(10):
    print(a, end=' ')
    a, b = b, a + b
n = int(input("Сон киритинг: "))
fact = 1
for i in range(1, n+1):
    fact *= i
print(f"{n}! = {fact}")
list1 = [1, 1, 2]
list2 = [2, 3, 4]
from collections import Counter

def uncommon(list1, list2):
    c1 = Counter(list1)
    c2 = Counter(list2)
    result = []

    for key in c1:
        if key not in c2:
            result.extend([key] * c1[key])
    for key in c2:
        if key not in c1:
            result.extend([key] * c2[key])
    return result
print(uncommon([1, 1, 2], [2, 3, 4]))         # [1, 1, 3, 4]
print(uncommon([1, 2, 3], [4, 5, 6]))         # [1, 2, 3, 4, 5, 6]
print(uncommon([1, 1, 2, 3, 4, 2], [1, 3, 4, 5]))  # [2, 2, 5]
