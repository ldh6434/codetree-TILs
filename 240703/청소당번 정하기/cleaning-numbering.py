school = 0
hall = 0
bath = 0
n=int(input())
for i in range(1, n):
    if i % 12 == 0:
        bath +=1
    elif i % 3 == 0:
        hall +=1
    elif i % 2 == 0:
        school +=1
print (school, hall, bath)