T = int(input())
memo = [[0 for _ in range(11)] for _ in range(11)]
for i in range(10):
    for j in range(i+1):
        if j == 0 or i == j:
            memo[i][j] = 1
        else:
            memo[i][j] = memo[i-1][j-1] + memo[i-1][j]
for tc in range(1, T+1):
    N = int(input())
    print(f'#{tc}')
    for i in range(N):
        for j in range(i+1):
            print(f'{memo[i][j]}', end = " ")
        print()

# t = int(input())
# for case in range(1, t + 1):
#     n = int(input())
#
#     memo = [[0] * n for _ in range(n)]
#
#     for i in range(n):
#         for j in range(i + 1):
#             if j == 0 or i == j:
#                 memo[i][j] = 1
#             else:
#                 memo[i][j] = memo[i - 1][j - 1] + memo[i - 1][j]
#     print(f'#{case}')
#     for lst in memo:
#         result = [x for x in lst if x]
#         print(*result)