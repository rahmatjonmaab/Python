mevalar = ['Anor', 'banan', 'gilos', 'shaftoli', 'uzum']
print(mevalar[2]) 
a = [1, 2, 3, 7, 8, 9]
b = [4, 5, 6, 0, 10, 11]
c = a + b
print(c)
sonlar = [10, 20, 30, 40, 50, 60, 70, 80, 90]
yangi = [sonlar[0], sonlar[len(sonlar)//2], sonlar[-1]]
kinofilmlar = ['Shum bola', 'Toylar muborak', 'Suyunchi', 'Shaytanat', 'Titanic']
natija = tuple(kinofilmlar)
print(natija)
shaharlar = ['Tashkent', 'Ostana', 'Paris', 'Rome', 'Dushanbe']
print("Paris" in shaharlar)
sities = ['London', 'Paris', 'Rome']
print("Paris" in sities)
a = [1, 2, 3, 4]
b = a * 3
print(b)
a = [100, 200, 300, 400, 500]
a[0], a[-1] = a[-1], a[0]
print(a)
s = tuple(range(1, 11))
print(s[2:7])
ranglar = ['qora', 'kok', 'oq', 'sariq', 'oq', 'oq rang']
print(ranglar.count('oq'))
hayvonlar = ('it', 'ayiq', 'yolbars', 'sher')
print(hayvonlar.index('sher'))
a = (20, 2, 20)
b = (40, 2, 40)
c = a + b
print(c)
a = [1, 2, 3, 4]
b = (5, 6, 7, 8)
print(len(a))
print(len(b))
a = [1, 2, 3, 4, 9, 10]
b = (5, 6, 7, 8)
print(len(a))
print(len(b))
a = (1, 2, 3, 4, 5)
b = list(a)
print(b)
a = (50, 40, 30, 20, 10)
b = list(a)
print(b)
a = (1, 10, 5, 9, 0, 8, 6, 7)
print(max(a))
print(min(a))
sozlar = ('sayoxat', 'dunyo', 'KITOB', 'salom')
print(sozlar[::-1])
