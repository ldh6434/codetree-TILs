cnt=0
cny=0
for i in range(10):
    n = int(input())
    if n % 3 == 0:
        cnt += 1
    if n % 5 == 0:
        cny += 1
print(cnt, cny)