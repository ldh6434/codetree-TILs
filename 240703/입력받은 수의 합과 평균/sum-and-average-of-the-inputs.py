n = int(input())
sum = 0
sum1 = 0
for i in range(n):
    n = int(input())
    if n >= 1:
        sum += n
        sum1 += 1
avg = sum / sum1
print(sum, "%.1f"%avg)