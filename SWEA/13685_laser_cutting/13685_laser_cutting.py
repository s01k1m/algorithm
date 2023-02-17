import sys

sys.stdin = open("input.txt")

def count(lst):
    ans = 0 # 총 막대의 갯수
    cnt = 0 # 추가되는 막대의 갯수
    n = len(lst)
    for i in range(n):
        if lst[i] == '(':       # ( 라면
            cnt += 1            # 막대 생성
        else:                   # ) 라면
            if lst[i-1] == '(': # () 라서 레이저 컷팅
                cnt -= 1        # 잘못 생성한 마지막 막대를 제거
                ans += cnt
            elif lst[i-1] == ')': # ))라면
                cnt -= 1          # 막대 한개가 끝에 도달함
                ans += 1          # 끝이난 막대 1조각 결과에 더해줌

    return ans


T = int(input())
for test_case in range(1, T+1):
    lst = list(input())

    ans = count(lst)

    print(f'#{test_case} {ans}')