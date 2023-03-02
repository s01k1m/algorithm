import sys
sys.stdin = open("input.txt", "r")


def fly(m, n, arr):
    lst = []
    for i_frontier in range(n - m + 1):
        for j_frontier in range(n - m + 1):
            box = []
            for i_flapper in range(i_frontier, i_frontier+m):
                for j_flapper in range(j_frontier, j_frontier+m):
                    box.append(arr[i_flapper][j_flapper])
            lst.append(sum(box))
    return lst



T = int(input()) # test case
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]


    print(f'#{tc} {max(fly(m, n, arr))}')

