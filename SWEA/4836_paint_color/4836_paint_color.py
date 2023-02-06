import sys
sys.stdin = open("input.txt")
# (r1, c1, r2, c2 color) = top left  x coordinates, top left  x coordinates, bottom right x coordinates,
# bottom right y coordinates, color number

# T = test case (1<= T <=50)
# N = number of times of paint color
T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 색칠하는 횟수
    info_colors = [] # 컬러 정보를 리스트로 정리할 것이다.
    for _ in range(N):
        color = list(map(int, input().split()))
        info_colors.append(color)
    # 이제 공간에 색을 칠할 것임
    # 공간을 만들어줌 10 *10 격자임 2차원 리스트 , 행렬로 만들 것이다.
    space = []

    for x in range(10):
        row =[]
        for y in range(10):
            row.append(0)
        space.append(row)
    # [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[],... ]


    for i in info_colors: #색칠하기 위해 컬러 정보를 순회함
        # i는 [r1, c1, r2, c2, color]이렇게 생겼음
        r1, c1, r2, c2, color = i
        for x in range (r1, r2+1):
            for y in range (c1, c2+1):
                if space[x][y] != color and space[x][y] < 3: #만약 좌표에 그 색깔이 없다면
                    space[x][y] = space[x][y] + color # 색을 칠해줌(색을 더해줌)


    cnt = 0
    for x in range (10): #space를 다 순회할 것이다.
        for y in range (10):
            if space[x][y] == 3: # 빨+파 이면 3이다.
                cnt += 1

    print(f'#{tc} {cnt}')


