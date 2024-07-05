n = int(input())
satisfied=True
for i in range(1,n):
    if i % n == 0 :
        satisfied=False
if satisfied==True:
    print('P')
else:
    print('C')