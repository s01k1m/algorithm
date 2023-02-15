# 7 8
# 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
#

# V: 정점 , E : 간선
V, E = map(int, input().split())

data = list(map(int, input().split()))

arr = [[0] * (V + 1) for _ in range(V + 1)]

visited = [0] * (V + 1) # 방문 여부 확인하는 list

for i in range(E): # E인게 이해가 안됨
	n1, n2 = data[i * 2], data[i * 2 + 1]
	arr[n1][n2] = 1 # = n1과 n2는 인접해있다
	arr[n2][n1] = 1


def dfs(v): # v: 지금현재 탐색하는 정점
	visited[v] = 1
	print(v, end = " ")
	# 현재 v는 시작정점, 인접한 정점 중 방문을 안한 곳
	for w in range(1, V + 1): # v+1 인게 어려워요우
		if arr[v][w] == 1 and visited[w] == 0:
			dfs(w)

dfs(1)
