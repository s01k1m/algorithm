
def bfs(si, sj, ei, ej):
    '''
    아래 주석을 문서화 주석, 영으로 docstring
    :param si: 시작점 행
    :param sj: 시작점 열
    :param ei: 도착점 행
    :param ej: 도착점 열
    :return: if it can escape return 1. if not, return 0
    '''
    q = []
    v = [[0]*M for _ in range(N)]

    q.append((si, sj))
    v[si][sj] = 1

    while q:
        ci, cj = q.pop(0)
        # 정답 처리
        if (ci, cj) == (ei, ej):
            return v[ei][ej]
        # 북, 남, 서, 동 탐색
        for di, dj in ((-1,0), (1,0), (0,-1),(0,1)):
            ni, nj = ci+di, cj+dj
            if 0 <= ni < N and 0<= nj < M and arr[ni][nj] == 1 and v[ni][nj] == 0:
                q.append((ni,nj))
                v[ni][nj] = v[ci][cj] + 1


N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]

ans = bfs()
print(ans)