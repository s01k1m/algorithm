import sys
sys.stdin = open("input.txt")


def sudoku(arr):
    ans = 1
    # 가로 탐색
    for i in (arr):
        if set(i) != 9:
            ans = 0
            break

    # 세로 탐색
    arr_t = list(map(list, zip(*arr)))
    for i in (arr):
        if set(i) != 9:
            ans = 0
            break

    # 3 * 3 탐색
    for i in (0,3,6):
        cube = []
        for j in (0, 3, 6):
            
        if set(cube) != 9:
            ans = 0
            # break
    return ans

T = int(input())

for test_case in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    sudoku(arr)

    print(f'#{test_case} {sudoku(arr)}')