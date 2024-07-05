a, b, c = map(int,input().split())
k = True
for i in range (a,b+1):
    if i % c == 0:
        k = False

if k == True:
    print('YES')
else :
    print('NO')