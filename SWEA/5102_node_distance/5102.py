import sys
sys.stdin = open("input.txt")


'''
인접리스트 adjacency list

0,1,2,3,4,5,6 노드이므로
6개의 빈 리스트의 리스트를 만들고
노드를 인덱스로 연결되어있는 노드를 요소로 추가한다.



'''
# 너비 우선 탐색
def bfs(s, e):
    queue = []
    visited = [0]*(V + 1)

    queue.append(s)
    visited[s] = 1
    
    while queue:    # 탐색할 노드가 있을 때
        target = queue.pop(0)
        
        if target == e:             # 정답 처리
            return visited[e] - 1
        
        for n in adj[target]:       # 연결된 노드
            if visited[n] == 0:     # 미방문 노드
                queue.append(n)
                visited[n] = visited[target] + 1
    return 0        # 목적지를 방문하지 못한 경우
            





T = int(input())
for tc in range(1, T+1):
    # V : 노드의 개수
    # E : 간선의 개수
    V, E = map(int, input().split())
    adj = [[] for _ in range(V+1)]
    # 인접리스트 생성
    for _ in range(E):
        s, e = map(int, input().split())
        adj[s].append(e)
        adj[e].append(s)

    # start : 출발 노드
    # goal : 도착 노드
    start, goal = map(int, input().split())


    # ans : 연결되지 않은 경우 0 또는 출발에서 도착까지 최소 간선의 개수
    ans = bfs(start,goal)
    print(f"#{tc} {ans}")