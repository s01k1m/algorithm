import sys
sys.stdin = open("input.txt")

T = int(input()) # test case
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # N = 자연수의 갯수
    # M = 이동 수
    queue = list(map(int, input().split()))

    for _ in range(M):
        queue.append(queue.pop(0))

    print(f'#{tc} {queue[0]}')


