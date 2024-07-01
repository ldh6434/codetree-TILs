def print_sequence(c, n):
    if c == 'A':
        for i in range(1, n + 1):
            print(i, end=' ')
    elif c == 'D':
        for i in range(n, 1 - 1, -1):
            print(i, end=' ')
    else:
        print("Invalid input")

# 사용자 입력 받기
user_input = input("")
c, n = user_input.split()
n = int(n)

# 함수 호출
print_sequence(c, n)