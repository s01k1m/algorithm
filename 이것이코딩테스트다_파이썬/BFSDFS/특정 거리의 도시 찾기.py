# 철째 줄의 도시의 개수 N, 도로의 개수 m, 거리의 정보 k, 출발 도시의 번호 x
# BFS 로 풀거임
import sys
sys.stdin = open("input.txt")

N, M, K, X = map(int, input().split())
# print(N, M, K, X)

visited = [-1] * (N+1)
arr = [[] for _ in range(N+1) ]

for i in range(M):
    start, end = map(int, input().split())
    arr[start].append(end) 
# print(visited, arr)
def road(start_city, arr, visited):
    queue = []
    queue.append(start_city)
    visited[start_city] = 0
    # visited에는 이제 방문처리를 하면서 시작도시에서부터의 최단거리를 기록할 것이다.
    while queue:

        cnt = queue.pop(0) # 선입 선출
        for i in arr[cnt]:

            if visited[i] == -1:
                # 큐에 넣고 방문처리를 하는데 방문처리를 할때 거리를 넣어줘야함
                queue.append(i)
                visited[i] = visited[cnt]+1

road(X, arr, visited)       

for i in range(1, N+1):
    if visited[i] == K:
        print(i)

