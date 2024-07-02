a, b = map(int,input().split())
sum = 0
for i in range(a,b+1):
    if i >= a and b+1 >= i:
        sum += i
print(sum)