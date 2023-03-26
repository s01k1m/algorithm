N, M = map(int, input().split())


cnt = 0

# 나눗셈을 먼저 할 수 있는 한 많이 하기
while N >= M :
    if N % M == 0:
        N = N // M
        cnt += 1

# 나누어 떨어지지 않는 부분 빼기
while N != 1:
    N -= 1
    cnt += 1

print(cnt)