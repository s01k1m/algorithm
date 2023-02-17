import sys
sys.stdin = open("input.txt")



T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    i = 0
    ans = 0
    # [1]단계 i ~ 끝까지 최대값의 index 찾기
    while i < N:
        i_mx = i
        for j in range(i+1, N):
            if lst[i_mx] < lst[j]:
                i_mx = j
    # [2] i~i_mx 까지의 최대값과의 차이 누적
        for j in range(i, i_mx):
            benefit = lst[i_mx] - lst[j]
            ans += benefit

        i = i_mx + 1

    print(f'#{test_case} {ans}')
