sum = 0
while True:
    n = int(input())
    if n % 2 == 0:
        n = n // 2
        sum += 1
        print(n)
    if sum == 3:
        break