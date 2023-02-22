# g : 그래프
# v : 시작 노드
# n : 노드의 개수
def bfs(g, v, n):
    # 초기화
    # 방문 배열 만들기
    visited = [0] * (n + 1)
    # 큐 생성
    q = []
    # 시작지점 큐에 넣고 시작지점을 방문체크
    q.append(v)
    visited[v] = 1

    # 큐가 비어있다면 모두 탐색한 것으로 인식
    # 큐가 빌때까지 계속 반복한다.
    while q:
        # 큐의 맨 앞 원소 꺼내오기
        # 현재 위치를 t 라고 하자.
        t = q.pop(0)
        print(node[t])
        # t와 연결된 모든 노드에 대해서 탐색
        for nt in G[t]:
            # 방문하지 않은 정점 nt 만 골라서 방문
            if not visited[nt]:
                q.append(nt)
                visited[nt] = visited[t] + 1


#        0    1    2    3    4    5    6    7    8    9
node = ['x', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']

'''
노드의 개수 V
간선의 개수 E
V = 9
E = 8
9 8
1 2
1 3
1 4
2 5
2 6
4 7
4 8
4 9
'''

'''
7 8
1 2
1 3
2 4
2 5
4 6
5 6
6 7
3 7
'''

V, E = map(int, input().split())
# 인접리스트
G = [[] for _ in range(V + 1)]
# G[i] => i번 노드에 연결되어 있는 노드의 리스트
# 그래프 만들기 (인접리스트)
for i in range(E):
    start, to = map(int, input().split())
    G[start].append(to)
    G[to].append(start)

bfs(G, 1, V)
