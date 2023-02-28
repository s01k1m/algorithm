import sys
sys.stdin = open("input.txt")

# 돌이 가로, 세로, 대각선 중 하나의 방향으로 다섯 개 이상 연속한 부분이 있는지 없는지 판정하는 프로그램을 작성하라.

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    ans = "NO"
    while True:
        # 가로 검증
        for i in range(N):
            cnt = 0
            for j in range(N):
                if arr[i][j] == 'o':
                    cnt += 1
                    if cnt >= 5:
                        ans = "YES"
                        break
                else:
                    cnt = 0

        # 세로 검증
        for j in range(N):
            cnt = 0
            for i in range(N):
                if arr[i][j] == 'o':
                    cnt +=  1
                    if cnt >= 5:
                        ans = "YES"
                        break
                else:
                    cnt = 0

        # 대각선 검증 왼쪽 탑에서 아래 오른쪽
        cnt = 0
        for i in range(N):
            if arr[i][N-i-1] == "o":
                cnt += 1
                if cnt >= 5:
                    ans = "YES"
                    break
            else:
                cnt = 0

        # 대각선 검증 오른쪽 탑에서 왼쪽 아래
        cnt = 0
        for i in range(N):
            if arr[N-i-1][i] == "o":
                cnt += 1
                if cnt >= 5:
                    ans = "YES"
                    break
            else:
                cnt = 0

        break

    print(f'#{tc} {ans}')