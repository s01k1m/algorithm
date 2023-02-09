import sys
sys.stdin = open("input.txt")


T = int(input())

for _ in range(1, T+1):
    p = list(input())
    t = list(input())
    M = len(p)
    N = len(t)

    def bf2(p, t, N, M):
        ans = 0
        for i in p:
            cnt = 0
            for j in t:
                if j == i:
                    cnt += 1
            if cnt > ans:
                ans = cnt

        return ans



    print(f'#{_} {bf2(p, t, N, M)}')