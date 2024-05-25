# 'A'로 분류되는 사람의 수를 셀 변수
a_count = 0

# 3명의 입력을 받습니다.
for _ in range(3):
    symptom, temperature = input().split()
    temperature = float(temperature)
    
    # 조건에 따라 상태를 판별합니다.
    if symptom == 'Y' and temperature >= 37:
        a_count += 1

# 위급상황 여부를 출력합니다.
if a_count >= 2:
    print('E')
else:
    print('N')