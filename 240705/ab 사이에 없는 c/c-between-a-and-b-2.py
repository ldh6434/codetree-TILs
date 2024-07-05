a, b, c = map(int,input().split())
a = False
for i in range (a,b+1):
    if i % c != 0:
        a = True
if a == True:
    print('YES')
else :
    print('NO')