# 1. Sort a Dictionary by Value

# Луғатни қийматлар бўйича саралаш (кўпайиш ва камайиш тартибида) 
data = {'a': 3, 'b': 1, 'c': 2, 'd':4}

# КЎПАЙИШИ
print(dict(sorted(data.items(), key=lambda x: x[1])))

# КАМАЙИШИ
print(dict(sorted(data.items(), key=lambda x: x[1], reverse=True)))
# 2. Add a Key to a Dictionary 2. Lug'atga kalit qo'shing

# Lug'atga kalit qo'shish uchun Python skriptini yozin

data = {0: 10, 1: 20}
data[2] = 30
print(data)
data = {0: 10, 1: 20}
data[4] = 40
print(data)
    # 3. Concatenate Multiple Dictionaries 3. Bir nechta lug‘atlarni birlashtiring

    # Yangi lug'at yaratish uchun quyidagi lug'atlarni birlashtirish uchun Python skriptini yozing.

    dic1 = {1: 10, 2: 20}
    dic2 = {3: 30, 4: 40}
    dic3 = {5: 50, 6: 60}

    yangi = {**dic1, **dic2, **dic3}
    print(yangi)
# 4. Generate a Dictionary with Squares  4. Kvadratchalar bilan lug‘at yarating

# (x, x*x) ko'rinishida raqamni (1 va n oralig'ida) o'z ichiga olgan lug'at yaratish va chop etish uchun Python skriptini yozing.

n = 5
kvadratlar = {x: x*x for x in range(1, n+1)}
print(kvadratlar)
# 5. Dictionary of Squares (1 to 15) 5. Kvadratchalar lug'ati (1 dan 15 gacha)

# Lug'atni chop etish uchun Python skriptini yozing, bu erda kalitlar 1 dan 15 gacha bo'lgan raqamlar (ikkalasi ham kiritilgan) va qiymatlar kalitlarning kvadratidir.

kvlar = {x: x*x for x in range(1, 17)}
print(kvlar)
# 1. Create a Set 1. To'plam yarating

# To'plam yaratish uchun Python dasturini yozing.

my_set = {1, 2, 3, 4, 5}
print(my_set)
# 2. Iterate Over a Set 2. To'plam ustida takrorlash

# To'plamlarni takrorlash uchun Python dasturini yozing.

my_set = {10, 20, 30, 40, 50}
for item in my_set:
    print(item)
  my_set = {1, 2, 3, 4, 5}
for item in my_set:
    print(item)
  # 3. Add Member(s) to a Set 3. To'plamga a'zo(lar)ni qo'shing

# To'plamga a'zo(lar)ni qo'shish uchun Python dasturini yozing.

my_set = {1, 2, 3, 4, 5}
my_set.add(6)
print(my_set)
my_set = {1, 2}
my_set.add(3)
print(my_set)
# 4. Remove Item(s) from a Set 4. To'plamdan element(lar)ni olib tashlang

# Berilgan to'plamdan element(lar)ni olib tashlash uchun Python dasturini yozing.

my_set = {1, 2, 3, 4, 5, 7, 8, 9, 10}
my_set.remove(2:, 1)
print(my_set)
my_set = {1, 2, 3}
my_set.remove(2)
print(my_set)
# 5. Remove an Item if Present in the Set 5. To'plamda mavjud bo'lsa, elementni olib tashlang
# Agar to'plamda mavjud bo'lsa, to'plamdan elementni olib tashlash uchun Python dasturini yozing.

my_set = {1, 2, 3, 2, 4, 9, 2}
my_set.discard(2)  
print(my_set)
