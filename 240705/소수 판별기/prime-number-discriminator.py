import math

# 소수 판별 함수
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# 숫자 입력
n = int(input().strip())

# 소수 여부 출력
if is_prime(n):
    print("P")
else:
    print("C")