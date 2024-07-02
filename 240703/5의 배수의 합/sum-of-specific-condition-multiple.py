a, b = map(int,input().split())
sum = 0
for i in range(a,b+1):
    if a > b :
        if i % 5 == 0:
            sum += i
    elif a < b :
        if i % 5 == 0:
            sum += i
    else :
        print(i)
print(sum)