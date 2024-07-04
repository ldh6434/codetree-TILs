average = 0
sum = 0
sum1 = 0
while True:
    n = int(input())
    if n >= 20 and n <= 29:
        sum += n
        sum1 += 1
    else:
        average = sum / sum1
        print(f"{average:.2f}")
        break