T = int(input())

def mx_num(lst):
    mx = lst[0]
    for i in (lst):
        if mx <= i:
            mx = i
    return mx


for _ in range(1, T+1):
    N = int(input()) # 테스트 케이스 길이
    divs = list(map(int, list(input()))) #테스트 케이스 리스트로 저장
    cnts = [1] * N # 카운트 리스트 만들어 줌
    cnt = 0

    for i in range(1, N):
        if divs[i] == 1:
            if divs[i-1] == 1:
                cnt += 1
                cnts[i] = cnts[i] + cnt
        else:
            cnt = 0
        mx = mx_num(cnts)


    print(f'#{_} {mx}')