def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
print(is_prime(4))
print(is_prime(7))
def digit_sum(k):
    return sum(int(r) for r in str(k))
print(digit_sum(24))   
print(digit_sum(502))  
def powers_of_two(N):
    i = 1
    while 2**i <= N:
        print(2**i, end=' ')
        i += 1
