import sys
sys.stdin = open("input.txt")

T = int(input()) # test case

def paper(n):
    if n == 10:
        return 1
    elif n == 20:
        return 3
    elif n < 10:
        return 0
    else:
        return paper(n-10) + (2 * paper(n-20))

for tc in range(1, T+1):
    N = int(input()) # 바닥 길이, 10의 배수만 들어올 수 있다.

    print(f"#{tc} {paper(N)}")

'''
재귀함수였음ㅋㅋㅋ
수열이라..ㅋㅋㅋ
뻘짓했다.. 엑셀로 사각형 2n개 그리고 앉았음..ㅋㅋ
'''