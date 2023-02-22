'''
달팽이 슈도 코드
<기하학 도형은 손으로 무조건 적고
 지그재그 해보든가 꼭 해보세요>
1 <= N <= 10

달팽이는 1부터 N*N까지의 숫자가

[0][0] = 1 오른쪽 방향으로(dr 변수 설정)
범위 이내 & 이동할 위치의 값 == 0: dr ( 오른쪽, 아래, 왼쪽, 위쪽) 0 1 2 3 방향을 적어놓으면 반복하겠지
범위 밖 : dr 꺾어서/ 방향을 꺽어야한다. next_j, next_i

for cnt (1, N*N + 1)
    arr[i][j] <- cnt를 적어준다
    ni, nj = i + di[dr], j + dj[dr]
    if 0 <= nj < N and o <=nj <N and ==0
        i, j = ni, nj
    else # 꺽어서 이동
        dr = (dr + 1) % 4
        i, j = i + di[dr], j + dj[dr]

'''


# di dj -> 아래 <- 위 만들기

import sys
sys.stdin = open("input.txt")

T = int(input())
for test_case in range(1, T+1):
    # N arr 만들기
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    # i, j ,dr 초기값 만들기
    i = 0
    j = 0
    dr = 0 # dr은 (di, dj)의 방향 4가지로 인덱스 값으로 사용될 것이다.
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    # for cnt in range(1, N * N +1)만들기
    # for 문은 숫자를 적기 위한 것이다
    # 방향을 설정하면 그곳에 cnt 를 넣을 것이다.
    for number in range(1, N * N + 1):
        arr[i][j] = number
        # 다음 좌표 계산
        next_i, next_j = i + di[dr], j + dj[dr]
        # if (이동할 위치가 배열의 범위 내이고 이동할 위치값이 0)이면
        if 0 <= next_i < N and 0 <= next_j < N and arr[next_i][next_j] == 0:
            i, j = next_i, next_j
        # 이동하도록 i, j 재설정
        # else: 방향을 꺽어서 이동한다.
        else:
            dr = (dr+1) % 4
            i , j = i + di[dr], j+ dj[dr]
# 프린트
    for lst in arr:
        print(*lst)
