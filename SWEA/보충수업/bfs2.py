dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def is_valid(r, c):
    return 0 <= r < n and 0 <= c < n


# sr : 시작 행
# sc : 시작 열
def bfs(sr, sc):
    visited = [[0] * n for _ in range(n)]

    q = []
    q.append((sr, sc))  # 시작점 sr, sc 를 큐에 삽입
    visited[sr][sc] = 1

    while q:

        r, c = q.pop(0)

        if maze[r][c] == 99:
            print(f"탈출")
            break

        maze[r][c] = visited[r][c]

        for i in range(n):
            for j in range(n):
                if (i, j) == (r, c):
                    print("★", end=" ")
                else:
                    print(maze[i][j], end=" ")
            print()

        print("==================")

        # 현재 위치 r,c 기준으로 상하좌우 4방향 탐색
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            # 내가 계산한 nr, nc가 유효한 위치인지 확인하고,
            # 유효한 위치라면 다음 탐색 위치에 (큐) 추가한다.
            # 2차원 배열의 범위안, 벽이아님, 방문한적이 없음
            if is_valid(nr, nc) and maze[nr][nc] != 1 and not visited[nr][nc]:
                q.append((nr, nc))  # 큐에 넣기
                # bfs 단계 처리
                visited[nr][nc] = visited[r][c] + 1


n = 5

maze = [[0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 1, 3, 1, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0]]

maze = [[0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]]

bfs(2, 2)
