from collections import deque

# M = column
# N = row
M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]


def find_tomatoes(arr, queue):
    # 토마토(1)을 찾는 함수
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                queue.append((0, i, j))


queue = deque()
find_tomatoes(arr, queue)  # 이제 큐에는 day0의 토마토의 좌표가 들어간다.
visited = [[0] * M for _ in range(N)]  # 토마토의 좌파 방문 여부 체크 할 비지티드
# 델타탐색하면서 이미 익은 토마토를 또 중복처리하는 것을 막기 위해서

day = 0
while queue:
    cnt, x, y = queue.popleft()  # 퇌토의 좌표를 불러왔음
    day = max(day, cnt)
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:  # 십자방향 토마토를 익게 한다.
        nx = x + dx
        ny = y + dy

        if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 0:
            arr[nx][ny] = 1

            queue.append([cnt + 1, nx, ny])

# day를 어디서 +1 하냐.ㅜㅜ
if [1 for r in range(N) for c in range(M) if arr[r][c] == 0]:
    day = -1

print(day)