n = int(input())
realn = n
sum = 0
for i in range(1,realn+1):
    if n > 1:
        n = n // i
        sum += 1
    else:
        break
print(sum)