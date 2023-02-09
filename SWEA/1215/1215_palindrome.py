import sys
sys.stdin = open("input.txt")

T = 10

N = 8
for tc in range(1, 1+T):
    M = int(input())
    lst = []
    arr = [list(map(str, input())) for _ in range(N)]
    arr2 = list()
    for i in range(8):
        row = []
        for j in range(8):
            row.append(arr[j][i])

        arr2.append(row)

    for i in range(N):
        for j in range(N-M+1):
            if arr[i][j:j+M] == arr[i][j:j+M][::-1]:
                lst.append(arr[i][j:j+M])

    for j in range(N-M+1):
        for i in range(N):
            s = ''
            for k in range(M):
                s = s + arr[j + k][i]
            if s == s[::-1]:
                lst.append(s)
    print(f'#{tc} {len(lst)}')