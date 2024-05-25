num1 = input().split()
age1 = int(num1[0])
sex1 = num1[1]

num2 = input().split()
age2 = int(num2[0])
sex2 = num2[1]

if (age1 >= 19 and sex1 =='M') or (age <= 19 or sex2 == 'M') :
    print(1)
else :
    print(0)