# BFS why? 가까운곳에서 먼곳으로 /인접한 칸의 0을 탐색해야한다.


import sys
sys.stdin = open("input.txt")

from collections import deque
N, M = map(int, input().split())
arr = [list(map(int, list(input()))) for _ in range(N)]

visited = [[0] * M for _ in range(N)]
cnt = 0


def bfs(arr, sx, sy, visited):
    global cnt
    queue = deque()
    queue.append([sx, sy])
    visited[sx][sy] = 1
    while queue:
        x, y = queue.popleft()
        for dx, dy in [[1, 0], [-1, 0], [0, -1], [0, 1]]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0 and arr[nx][ny] == 1:
                queue.append([nx, ny])
                arr[nx][ny] = arr[x][y] + 1
                visited[nx][ny] = 1




for i in range(N):
    for j in range(M):
        if arr[i][j] == 1 and visited[i][j] == 0:
            bfs(arr, i, j, visited)


print(arr[N-1][M-1])
