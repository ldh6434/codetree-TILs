a = int(input())

if a <= 7:
    if a % 2 == 0:
        if a == 2:
            print('28')
        else:
            print('30')
    else:
        print('31')
else:
    if a % 2 == 0:
        print('31')
    else:
        print('30')