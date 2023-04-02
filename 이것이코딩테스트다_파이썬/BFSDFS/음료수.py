# BFS why? 가까운곳에서 먼곳으로 /인접한 칸의 0을 탐색해야한다.
from collections import deque
import sys
sys.stdin = open("input.txt")

N, M = map(int, input().split())
arr = [list(map(int, list(input()))) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
cnt = 0
# v =(x, y)
def bfs(arr, v, visited):
    global cnt
    queue = deque([v])
    visited[v[0]][v[1]] = True
    while queue:
        x, y = queue.popleft()
        for dx, dy in [[1,0], [-1,0], [0,-1], [0,1]]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
                bfs(arr, (nx, ny), visited)
    cnt += 1

for i in range(N):
    for j in range(M):
        if arr[i][j] == 0 and visited[i][j] == 0:
            bfs(arr, (i, j), visited)

print(cnt)