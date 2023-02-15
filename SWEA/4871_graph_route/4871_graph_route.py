import sys

sys.stdin = open("input.txt")

# DFS 탐색 재귀함수
def dfs(s, v): # s: 출발 노드 , v : 노드 수
    visited[s] = 1
    # 탐색(간선으로 갈 수 있는)한 노드 넣어줌
    route.append(s)

    for w in range(1, v+1):
        if arr[s][w] == 1 and visited[w] ==0:
            dfs(w, v)




T = int(input()) # test case
for tc in range(1, T+1):
    # V : 노드 수
    # E : 간선 수
    V, E = map(int, input().split())
    # 인접 행렬
    arr = [[0] * (V + 1) for _ in range(V + 1)]

    # 간선 정보 가져옴
    for _ in range(E):
        i, j = map(int, input().split())
        arr[i][j] = 1


    # 탐색 가능한 노드를 넣어줄 route 리스트
    route = []

    #
    visited = [0] * (V+1)

    # S : 출발 노드
    # G : 도착 노드
    S, G = map(int, input().split())

    dfs(S, V)

    ans = 0
    # route 안에 S와 G 다있으면 ans = 1
    if S in route and G in route:
        ans = 1

    print(f'#{tc} {ans}')