import sys
sys.stdin = open("input.txt")

def bfs (si, sj, N):
    queue = []
    visited = [[0] * N for _ in range(N)]

    queue.append((si, sj))
    visited[si][sj] = 1

    while queue:
        ci, cj = queue.pop(0)
        if arr[ci][cj] == 3:            # 목적지에 도달한 경우
            return visited[ci][cj] - 2

        # 4방향, 범위, 미방문이며 1이 아니면(벽이 아닌 경우)
        for di, dj in ((-1, 0), (1, 0), (0,-1), (0, 1)):
            ni, nj = ci+di, cj+dj
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] != 1 and visited[ni][nj] == 0:
                queue.append((ni, nj))
                visited[ni][nj] = visited[ci][cj]+1     # 몇번 이동했는지 알려줌
    return 0                        # 목적지에 도달하지 못한 경우


T = int(input())
for test_case in range(1, T+1):
    N = int(input())                                    # N : 미로의 크기
    arr = [list(map(int, input())) for _ in range(N)]   # arr : 미로 데이터 2차원 행렬


    # si, sj 즉 시작점 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                si, sj = i, j

    ans = bfs(si, sj, N)
    print(f'#{test_case} {ans}')