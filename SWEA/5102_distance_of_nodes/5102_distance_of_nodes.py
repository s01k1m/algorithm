import sys
sys.stdin = open("input.txt")


T = int(input())

for tc in range(T):
    V, E = map(int, input().split())

    arr = [[0] * (V + 1) for _ in range(V + 1)]

    visited = [0] * (V + 1)  # 방문 여부 확인하는 list

    for i in range(E):  # E인게 이해가 안됨
        n1, n2 = map(int, input().split())
        arr[n1][n2] = 1  # = n1과 n2는 인접해있다
        arr[n2][n1] = 1

    start, end = map(int, input().split())
    ans = 0

    def dfs(s, e):  # v: 지금현재 탐색하는 정점
        if s == e:
            visited[s] = 1
            return
        else:
            visited[s] = 1
            # 현재 v는 시작정점, 인접한 정점 중 방문을 안한 곳
            for w in range(1, V + 1):  # v+1
                if arr[s][w] == 1 and visited[w] == 0:
                    ans +=1
                    dfs(w, e)
    print(visited)

    dfs(start, end)

    if visited[start] == 1 and visited[end] == 1:
        ans = sum(visited)

    print(ans)