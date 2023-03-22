import sys
sys.stdin = open("input.txt")

# Testcase
T = int(input())
for tc in range(T):
    na, *a = map(int, input().split())
    nb, *b = map(int, input().split())
    a.sort(reverse=True)    # 역순으로 정렬
    b.sort(reverse=True)
    if a == b:          # 그림이 같으면
        print("D")      # 무승부
    else:
        n = na
        if na > nb:     # 그림 갯수가 적은 사람을 기준으로 for문 순회
            n = nb
        for i in range(n):
            if a[i] == b[i]:            # a, b 그림이 일치하면
                if i == n-1:            # 둘 중 하나가 서로의 부분집합일때
                    if n < nb:          # 더 길이가 긴 쪽(그림을 더 많이 가진)이 승리
                        print('B')      # B 승리
                    else:
                        print('A')
                pass
            elif a[i] > b[i]:
                print('A')
                break
            elif a[i] < b[i]:
                print('B')
                break

