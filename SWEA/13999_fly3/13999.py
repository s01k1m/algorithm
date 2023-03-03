# 델타 탐색 응용 문제

# 델타 탐색이 물결처럼 확장되는 형태이다.

import sys
sys.stdin = open("input.txt")


T = int(input())        # T : 테스트 케이스
for tc in range(1, T+1):
    # N : N * N 행렬의 N 크기
    # M : 스프레이의 분사 세기.
    N, M = map(int, input().split())
    # arr : 영역에 존재하는 파리 2차원 리스트
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    # 십자 방향 탐색
    for i in range(N):
        for j in range(N):
            # 중심값
            fly1 = arr[i][j]
            # 델타 탐색 동, 남, 서, 북 방향으로 파리 잡기
            
            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:    # 동, 남, 서, 북
                for m in range(1, M): # 스프레이의 크기 만큼 본인은 앞에서 더해줘서 M-1 만큼 스프레이가 퍼진다.
                    ni = i + di*m
                    nj = j + dj*m
                    if 0 <= ni < N and 0 <= nj < N:     # 유효한 좌표일 때
                        fly1 += arr[ni][nj]             # 잡을 수 있는 파리에 더해줌
            ans = max(ans, fly1)

            # 모서리 방향 탐색
            fly2 = arr[i][j]
            # 델타 탐색 모서리 확대 방향으로 파리 잡기

            for di, dj in [(-1, 1), (1, 1), (1, -1), (-1, -1)]:    # 우상, 우하, 좌하, 좌상
                for m in range(1, M):
                    ni = i + di*m
                    nj = j + dj*m
                    if 0 <= ni < N and 0 <= nj < N:
                        fly2 += arr[ni][nj]
            ans = max(ans, fly2)

    print(f"#{tc} {ans}")
    


