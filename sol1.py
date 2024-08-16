import sys
sys.stdin = open('input.txt')


for tc in range(1, 11):
    T = int(input())
    password = list(map(int, input().split()))
    while not password[-1] == 0:
        for i in range(1,6):
            if password[0] - i <= 0:
                password.append(max(password.pop(0) - i,0))
                answer = password
                break
            else:
                password.append(password.pop(0) - i)
    print(f'#{tc}', *answer)
