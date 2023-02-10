import sys
sys.stdin = open("input.txt")

# K의 길이 단어가 최대 몇번 들어갈 수 있는 지 ans에 담아 리턴한다

def count(arr):
    ans = 0
    for lst in arr:
        cnt = 0
        for n in lst:
            if n == 1:
                cnt += 1 # 단어를 널을 수 있는 칸
            else:       # 칸 없음
                if cnt == K:
                    ans += 1
                cnt = 0
    return ans


T = int(input())
for test_case in range(1, T+1):
    M, K = map(int, input().split())
    arr = [list(map(int, input().split())) + [0] for _ in range(M)] + [[0]*(M+1)]
    # making vertical arr as arr_t separately
    arr_t = list(zip(*arr)) # array transform
    ans = count(arr) + count(arr_t)
    print(f'#{test_case} {ans}')



