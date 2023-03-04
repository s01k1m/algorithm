import sys

sys.stdin = open("input.txt")

def position(arr, H, W):
    for i in range(H):
        for j in range(W):
            if arr[i][j] in ['^', 'v', '<', '>']:
                return [i, j]


T = int(input())
for tc in range(1, T + 1):
    # H : 맵 높이
    # W : 맵 너비
    H, W = map(int, input().split())
    # arr : 맵
    arr = [list(input()) for _ in range(H)]
    # N : 사용자가 넣을 입력의 개수
    N = int(input())
    # inp : 사용자가 입력한 문자열
    inp = input()
    # ans : 사용자가 입력한 문자열 수행 후의 맵

    # 문자에 다른 동작 dictionary
    move = {'U': [-1, 0], 'D': [1, 0], 'L': [0, -1], 'R': [0, 1]}
    # ['^', 'v', '<', '>']

    for n in range(N):
        if inp[n] == 'S':
            # 포탄 발사
            ci, cj = position(arr, H, W)
            direction = arr[ci][cj]
            # 포탄이 발사되는 방향으로 벽돌이 있다면 맵을 벽돌(*)에서 평지(.)로 바꿔주면 된다.
            if direction == '^':
                # 무엇을 돌아야하는 지 생각해보자
                # 위로 순회 포탄이 올라가야한다.
                for di in range(1, H):
                    # 포탄이 날아가는 장소가 맵을 벗어나지 않고, 벽돌이라면
                    if 0 <= ci - di < H and arr[ci - di][cj] == '*':
                        arr[ci - di][cj] = '.'  # 벽돌벽은 부서져서 평지가 되고 포탄은 없어져서 탈출
                        break
                    elif 0 <= ci - di < H and arr[ci - di][cj] == '#':  # 강철 벽 만나면 포탄 없어진다
                        break

            elif direction == 'v':
                # 아래로 내려가야한다
                for di in range(1, H):
                    # 포탄이 날아가는 장소가 맵을 벗어나지 않고, 벽돌이라면
                    if 0 <= ci + di < H and arr[ci + di][cj] == '*':
                        arr[ci + di][cj] = '.'  # 벽돌벽은 부서져서 평지가 되고 포탄은 없어져서 탈출
                        break
                    elif 0 <= ci + di < H and arr[ci + di][cj] == '#':  # 강철 벽 만나면 포탄 없어진다
                        break

            elif direction == '<':
                # 왼쪽으로 날아가야한다
                for dj in range(1, W):
                    # 포탄이 날아가는 장소가 맵을 벗어나지 않고, 벽돌이라면
                    if 0 <= cj - dj < W and arr[ci][cj - dj] == '*':
                        arr[ci][cj - dj] = '.'  # 벽돌벽은 부서져서 평지가 되고 포탄은 없어져서 탈출
                        break
                    elif 0 <= cj - dj < W and arr[ci][cj - dj] == '#':  # 강철 벽 만나면 포탄 없어진다
                        break

            elif direction == '>':
                # 오른쪽로 날아가야한다.
                for dj in range(1, W):
                    # 포탄이 날아가는 장소가 맵을 벗어나지 않고, 벽돌이라면
                    if 0 <= cj + dj < W and arr[ci][cj + dj] == '*':
                        arr[ci][cj + dj] = '.'  # 벽돌벽은 부서져서 평지가 되고 포탄은 없어져서 탈출
                        break
                    elif 0 <= cj + dj < W and arr[ci][cj + dj] == '#':  # 강철 벽 만나면 포탄 없어진다
                        break

        else:
            if inp[n] == 'U':
                ci, cj = position(arr, H, W)
                # 방향 전환
                arr[ci][cj] = '^'
                # 바라보는 방향이 평지라서 한칸 이동할 수 있다면 이동한다.
                if 0 <= ci - 1 < H and arr[ci - 1][cj] == '.':
                    arr[ci][cj] = '.'
                    ci = ci - 1
                    cj = cj
                    arr[ci][cj] = '^'

            elif inp[n] == 'D':
                ci, cj = position(arr, H, W)
                # 방향 전환
                arr[ci][cj] = 'v'
                # 바라보는 방향이 평지라서 한칸 이동할 수 있다면 이동한다.
                if 0 <= ci + 1 < H and arr[ci + 1][cj] == '.':
                    arr[ci][cj] = '.'
                    ci = ci + 1
                    cj = cj
                    arr[ci][cj] = 'v'

            elif inp[n] == 'L':
                ci, cj = position(arr, H, W)
                # 방향 전환
                arr[ci][cj] = '<'
                # 바라보는 방향이 평지라서 한칸 이동할 수 있다면 이동한다.
                if 0 <= cj - 1 < W and arr[ci][cj - 1] == '.':
                    arr[ci][cj] = '.'
                    ci = ci
                    cj = cj - 1
                    arr[ci][cj] = '<'

            elif inp[n] == 'R':
                ci, cj = position(arr, H, W)
                # 방향 전환
                arr[ci][cj] = '>'
                # 바라보는 방향이 평지라서 한칸 이동할 수 있다면 이동한다.
                if 0 <= cj + 1 < W and arr[ci][cj+ 1] == '.':
                    arr[ci][cj] = '.'
                    ci = ci
                    cj = cj + 1
                    arr[ci][cj] = '>'

    print(f'#{tc}', end=" ")
    for line in range(H):
        print(''.join(arr[line]))
