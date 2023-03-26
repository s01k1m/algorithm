# M : row
# N : column
import sys
sys.stdin = open("input.txt")

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]


# a function "tomato" for finding a unripe tomato.
def tomato(arr):
    # if it finds a unripe tomato. goat is still True.
    global goat
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                goat = True
                return
            else:
                # if it can't find a unripe tomato. goat will become False.
                goat = False
# Dates required for tomatoes to ripen

day = 0
mx_day = N * M - 4 - 2

goat = False
tomato(arr)

while goat:
    arr2 = arr[::]
    # arr 다 돌면서 십자방향 다 발꿀거임
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                # dx, xy = [(0,1), (1,0), (0,-1), (-1,0)] 동, 남, 서, 북 델타 탐색
                for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    nx = i + dx
                    ny = j + dy
                    if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 0:
                        arr2[nx][ny] = 1
    # 아래 코드를 넣지 않으면 인접한 토마토로 인해 다음날 변했을 토마토가 for문에 계속 걸리게 되면서
    # 같은 날 익은 토마토를 찾지 못하게 된다.
    # 원본에서 익은 토마토를 찾아서 복사본에서 인접한 토마토를 익게 하고 이걸 마지막에 대입해주는 방식을 한다면
    # 같은 날짜안에서 익은 토마토 찾기가 가능해진다.
    arr = arr2

    day += 1
    if day >= mx_day:
        day = -1
        goat = False
    else:
        tomato(arr)

print(day)
