def is_leap(year):
   
    if not isinstance(year, int):
        raise ValueError("Yil butun son bo'lishi kerak.")
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
print(is_leap(2024))  
print(is_leap(1900))  
print(is_leap(2000))  
print(is_leap(1983))
n = int(input("Butun son kiriting: "))

if n % 2 == 1:
    print("Weird")
elif 2 <= n <= 5:
    print("Not Weird")
elif 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")
  # 3. Икки сон орасидаги ЖЎФТ сонларни топиш (LOOP-СИЗ)
#  Solution 1: if-else билан

a = 4
b = 10

start = a if a % 2 == 0 else a + 1  # жўфтдан бошлаймиз
evens = list(range(start, b+1, 2))  # 2 қадам билан
print(evens)
# Solution 2: if-else СИЗ — фақат max(), min() ва range()

a = 4
b = 10

evens = list(range(min(a, b) + min(a, b) % 2, max(a, b)+1, 2))
print(evens)
