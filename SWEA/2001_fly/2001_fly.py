import sys
sys.stdin = open("input.txt", "r")


T = int(input()) # test case

def fly(m, n, arr):
    for ii in range(m - n + 1):
        for i in range(m):
            sum = 0
            for j in range(ii, ii+n+1):
                # sum +=
                sum_lst.append(arr[i][j])


for tc in range(1, T+1):
    m, n = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(m)]
    sum_lst = []

    fly(m, n, arr)
    print(sum_lst)

