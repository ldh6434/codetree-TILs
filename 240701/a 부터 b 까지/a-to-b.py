a, b= map(int, input().split())
print(a, end=" ")
while a <= b:
    print(a, end=' ')
    if a % 2 == 1:
        a *= 2
    elif a % 2 == 0:
        a += 3