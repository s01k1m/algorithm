# DFS 문제

import sys
sys.stdin = open("test.txt")
T = int(input())

d = [(1,0), (-1,0), (0,-1), (0,1)]

def dfs(x, y, trail, K):
    global visited
    global d
    global ans
    # 현재까지 조성한 등산로가 크다면 ans를 바꿔준다.
    if ans < trail:
        ans = trail
    visited[x][y] = True
    for dx, dy in d:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:

            if arr[x][y] > arr[nx][ny]:
                dfs(nx, ny, trail+1, K)
            elif K and K > arr[nx][ny] - arr[x][y]:
                temp = arr[nx][ny]
                arr[nx][ny] = arr[x][y] - 1
                dfs(nx, ny, trail+1, 0)
                arr[nx][ny] = temp
    visited[x][y] = False


for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    stack = []
    visited = [[0]*N for _ in range(N)]
    ans = 0
    # 산 최고 높이 구하기
    mx = 0
    for i in range(N):
        for j in range(N):
            if mx < arr[i][j]:
                mx = arr[i][j]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == mx:
                dfs(i, j, 1, K)


    print(f'#{tc} {ans}')
