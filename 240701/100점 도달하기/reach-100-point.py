n = int(input())
for i in range(n, 100+1):
    if i >= 60 and i < 70 :
        print('D', end=" ")
    elif i >= 70 and i < 80 :
        print('C', end=" ")
    elif i >= 80 and i < 90 :
        print('B', end=" ")
    elif i >= 90 :
        print('A', end=" ")
    else :
        print('F', end=" ")