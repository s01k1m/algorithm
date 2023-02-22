dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def is_valid(r, c):
    return 0 <= r < n and 0 <= c < n


T = 10

for tc in range(1, T + 1):
    input()
    n = 16

    maze = [list(map(int, input())) for _ in range(n)]

    # 현재 위치
    r, c = 0, 0

    # 2라고 표시된 시작 지점 찾기
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                r, c = i, j

    # bfs 준비
    # 방문 배열 만들고
    # 큐 만들고, 큐에 시작 위치 삽입, 시작 위치 방문 표시
    visited = [[0] * n for _ in range(n)]

    visited[r][c] = 1
    q = []
    q.append((r, c))

    # 기본적으로 탈출할 수 없다고 생각, 중간에 3을 만나면 1로 바꿔주면 된다.
    ans = 0

    while q:
        r, c = q.pop(0)

        # 어느 순간 현재위치 r,c 가 3이 된다면 도착했다!!!!
        if maze[r][c] == 3:
            ans = 1
            break

        # r,c 기준으로 4방향 탐색
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            # 다음위치 계산후에 다음위치가 유효한지 검사
            # 2차원 배열 범위 안인지, 벽이 아닌지, 방문한적이 없는지
            if is_valid(nr, nc) and maze[nr][nc] != 1 and not visited[nr][nc]:
                q.append((nr, nc))
                visited[nr][nc] = 1

    print(f"#{tc} {ans}")