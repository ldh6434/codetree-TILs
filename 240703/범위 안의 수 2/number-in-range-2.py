sum = 0
avg = 0
for i in range(10):
    n = int(input())
    if n >= 0 and 200 >= n:
        sum += n
        avg += 1
average = sum / avg
print(sum, "%.1f"%average)