name = 'Azamat'
full_name = "Urazbaev Rahmatjon"
malumot = '''We are learing python
umumiy daraja'''
print()
s = "Salom dostlar"
print(s)
car = "LMaasleitbtui"
car[0:13:2]
car[1::2]
txt = 'MsaatmiazD'
txt[::2]
txt = 'MsaatmiazD'
print(txt[9:0:-2])
txt = "I'am John. I am from London"
print(txt[9:])
txt = input("Matn kiriting: ")
reversed_txt = txt[::-1]
print("Teskari matn:", reversed_txt)
print(input()[::-1])
soz = input("Iltimos so'z kiriting: ")

if soz.lower() == soz.lower()[::-1]:
    print("Bu so'z palindrom.")
else:
    print("Bu so'z palindrom emas.")
  txt = input("Matn kiriting: ")
vowels = 'AEIOUaeiou'
count = sum(1 for char in txt if char in vowels)
print("Unli harflar soni:", count)
txt = input("Iltimos matn kiriting: ")
print(txt[::-1])
print(sum(c in 'aeiouAEIOU' for c in input()))
print(max(map(int, input().split())))
s = input(); 
print(s == s[::-1])
S  = (input().split('@')[-1])
print
