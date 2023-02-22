import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range (1, T+1):
    N = int(input())                        # 당근의 갯수
    lst = list(map(int, input().split()))   # 당근의 크기
    result = 1
    cnt = 1

    for i in range(len(lst)-1):
        if lst[i] < lst[i+1]:
            cnt += 1

            if result < cnt:
                result = cnt
        else:
            cnt = 1

    print(f'#{tc} {result}')