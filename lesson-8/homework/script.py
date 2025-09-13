a = int(input("a ga qiynat kiriting:"))
for i in range(1,10):
    if a > 10:
        print(f"{i} ga bo'lgandagi qoldiq: {a%i}")
    elif 1 < a <= 10:
        if i <= a:
            print(f"{i} ga bo'lgandagi qoldiq: {a%i}")
        elif i > a:
            break
          try:
    n = int(input("n ni kiriting:"))
    if type(n) == int:
        print("Butun son")
    else:
        print("Butun emas")
except:
    print("Siz ValueError bilan xato qildingiz!")
  try:
    with open("test.txt", 'r') as f:
        print("Fayl topildi")
except:
    print("Siz FileNoteFaundError xatoligiga yo'l qo'ydingiz!")
  try:
    n = int(input("n ni kiriting:"))
    m = int(input("m ni kiriting:"))
    print("Siz son kiritdingiz")
except:
    print("Siz ValueError bilan xato qildingiz!")
  try:
    indeks = int(input("Sizga kerakli element indeksini kiriting!"))
    ls = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(f"{indeks}-element: {ls[indeks]}")
except:
    print(f"Ro'yxatda {len(ls)} ta element bor siz kiritgan indeks bo'yicha element topilmadi")
  try:
    x = input("n ga butun qiymat kiriting: ")

    if x == "":
        print("Siz hech narsa kiritmadingiz!")
    else:
        n = int(x)
        print("Siz kiritgan son:", n)

except ValueError:
    print("Iltimos, faqat butun son kiriting!")

except KeyboardInterrupt:
    print("\nSiz ma'lumot kiritishdan bosh tortdingiz (Ctrl+C bosildi).")
  try:
    a = 100
    for i in range(11):
        s = a // i
        print(s)
except ArithmeticError:
    print("Siz 0 ga bo'lishga urindingiz bu xato !!!")
  sonlar = [1, 2, 3]
def royxat_amali(royxat, metod, *args):
    try:
        # getattr - atributni olish uchun ishlatiladi
        funksiya = getattr(royxat, metod)
        natija = funksiya(*args)  # metodni chaqiramiz
        print(f"= '{metod}' metodi bajarildi.")
        return royxat if natija is None else natija

    except AttributeError:
        print(f"❌ Xatolik: '{metod}' nomli atribut yoki metod ro‘yxatda mavjud emas!")
        return None
      with open("namuna.txt", "r") as f:
    data = f.read()
    print(data)
n = int(input("n ni kiriting: "))

with open("namuna.txt", "r", encoding="utf-8") as f:
    for i in range(n):
        qator = f.readline()
        if not qator: 
            break
        print(qator.strip())
      with open('Uzbekistan.txt', 'w') as f:
    f.write('Uzbekistan is equal Uzbekiston')
with open('Uzbekistan.txt', 'r') as f:
    print(f.read())
n = int(input("n ni kiriting: "))
with open("namuna.txt", "r", encoding="utf-8") as f:
    qatorlar = f.readlines()
    oxirgi_qatorlar = qatorlar[-n:]
for qator in oxirgi_qatorlar:
    print(qator.strip())
with open("namuna.txt", "r", encoding="utf-8") as f:
    satrlar = [qator.strip() for qator in f.readlines()]
print(satrlar)
with open("namuna.txt", "r", encoding="utf-8") as f:
    satrlar = [qator.strip() for qator in f.readlines()]
print(satrlar)
import numpy as np

with open("namuna.txt", "r", encoding="utf-8") as f:
    royxat = f.read().splitlines() 
massiv = np.array(royxat)  
print(massiv)
with open("namuna.txt", 'r', encoding="utf-8") as f:
    data = f.read().split()
    max_uzunlik = max(len(soz) for soz in data)   
    eng_uzun_sozlar = [soz for soz in data if len(soz) == max_uzunlik] 
    
print("Eng uzun so'z(lar):", eng_uzun_sozlar)
print("Uzunligi:", max_uzunlik)
with open("namuna.txt", "r", encoding="utf-8") as f:
    qator_soni = sum(1 for _ in f)
    print("Qatorlar soni: ", qator_soni)
from collections import Counter
with open("namuna.txt", "r", encoding="utf-8") as f:
    data = f.read().split()
chastota = Counter(data)

for soz,soni in chastota.items():
    print(f"'{soz}': {soni} marta")
import os
fayl = "namuna.txt"
hajm_bayt = os.path.getsize(fayl)
hajm_kb = hajm_bayt / 1024
hajm_mb = hajm_kb / 1024

print(f"Fayl hajmi: {hajm_bayt} bayt")
print(f"Fayl hajmi: {hajm_kb:.2f} KB")
print(f"Fayl hajmi: {hajm_mb:.4f} MB")
ls = ["Python", "STATA", "C++", "Java", "JavaScript"]
with open("Uzbekistan.txt", 'a', encoding="utf-8") as f:
    f.write(", ".join(ls) + "\n")
with open("namuna.txt", "r", encoding="utf-8") as f:
    data = f.read()
with open("Uzbekistan.txt", 'w', encoding="utf-8") as f:
    f.write("".join(data) + "\n")
with open("Uzbekistan.txt", 'r', encoding="utf-8") as f:
    new_data = f.read()
    print(new_data)
with open("namuna.txt", "r", encoding="utf-8") as f:
    data = f.readlines()
    print(data)
with open("Uzbekistan.txt", 'a', encoding="utf-8") as f:
    f.write("".join(data) + "\n")
  mport random

# Faylni ochamiz
with open("namuna.txt", "r", encoding="utf-8") as f:
    qatorlar = f.readlines()  

# Tasodifiy qator tanlaymiz
tasodifiy_qator = random.choice(qatorlar)

print("Tasodifiy qator:", tasodifiy_qator.strip())
with open("namuna.txt", "r", encoding="utf-8") as f:
    qatorlar = f.readlines()
toza_qator = [qator.strip() for qator in qatorlar]
for q in toza_qator:
    print(q)
  with open("namuna.txt", "r", encoding="utf-8") as f:
    data = f.read().split()
    s = 0
    for i in data:
        s += 1
    print(f"Ro'yxat {s} ta so'z bor")
    import re

with open("namuna.txt", "r", encoding="utf-8") as f:
    matn = f.read()
sozlar = re.findall(r"\w+", matn)

print(f"Faylda {len(sozlar)} ta so'z bor")
import string

harflar = list(string.ascii_uppercase)  
for i in harflar:
    with open(f"{i}.txt", 'w', encoding='utf-8') as f:
        f.write(f'{i}')
      import string

harflar = list(string.ascii_uppercase)  
with open("harflar.txt", 'w', encoding='utf-8') as f:
    for i in harflar:
        f.write(f'{i} \n')
      harflar = list(string.ascii_uppercase)  # A–Z

n = 5  

with open("harflar.txt", 'w', encoding='utf-8') as f:
    for i in range(0, len(harflar), n):
        qator = " ".join(harflar[i:i+n])  # n ta harfni bitta qatorda yozamiz
        f.write(qator + "\n")
