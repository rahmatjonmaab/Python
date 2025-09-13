import threading
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def check_primes(start, end, result):
    for num in range(start, end):
        if is_prime(num):
            result.append(num)

def main():
    start = 1
    end = 50
    threads = []
    primes = []

    step = (end - start) // 4  # 4 ta thread uchun bo'lib chiqamiz

    for i in range(4):
        s = start + i * step
        if i == 3:
            e = end
        else:
            e = s + step
        # Har bir thread uchun natijalarni saqlash uchun alohida list yaratamiz
        temp = []
        t = threading.Thread(target=check_primes, args=(s, e, temp))
        t.temp = temp  # natijalarni olish uchun threadga qo'shamiz
        threads.append(t)
        t.start()

    all_primes = []
    for t in threads:
        t.join()
        all_primes.extend(t.temp)

    all_primes.sort()
    print("Topilgan tub sonlar:", all_primes)

if __name__ == "__main__":
    main()
  import threading

def count_words(lines, word_counts):
    local_counts = {}
    for line in lines:
        words = line.strip().split()
        for w in words:
            local_counts[w] = local_counts.get(w, 0) + 1
    word_counts.append(local_counts)

def main():
    filename = "large_text.txt"  # fayl nomi
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    threads = []
    word_counts_list = []
    n = 4
    step = len(lines) // n

    for i in range(n):
        start = i * step
        if i == n - 1:
            end = len(lines)
        else:
            end = start + step
        wc = []
        t = threading.Thread(target=count_words, args=(lines[start:end], wc))
        t.word_counts = wc
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    total_counts = {}
    for t in threads:
        for wc in t.word_counts:
            for word, count in wc.items():
                total_counts[word] = total_counts.get(word, 0) + count

    print("So'zlar soni:")
    for word, count in sorted(total_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()
