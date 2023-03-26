# N: row
# M: column

N, M = map(int, input().split())
arr = [ list(map(int, input().split())) for _ in range(N)]

mx = min(arr[0])

for i in range(1, N):
    num = min(arr[i])
    if mx < num :
        mx = num

print(mx)