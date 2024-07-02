a, b =map(int,input().split())
sum = 0
sum1 = 0
for i in range (a,b+1):
    if i % 7 == 0:
        sum += i
        sum1 += 1
    elif i % 5 == 0:
        sum += i
        sum1 += 1
avg = sum / sum1
print(sum, "%.1f"%avg )