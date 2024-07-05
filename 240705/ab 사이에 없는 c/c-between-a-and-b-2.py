a, b, c = map(int,input().split())
k = False
for i in range (a,b+1):
    if i % c != 0:
        k = True
        break
if k == True:
    print('YES')
else :
    print('NO')