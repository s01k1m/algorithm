T = int(input())


for tc in range(1, T+1):
    n = int(input())
    # 파스칼의 삼각형 구하기
    tri = [[0] * r for r in range(1, n+1)]

    # 한줄 씩 구하면서 출력
    # 이전 행에서 사용했던 결과를 이용해서 현재 행을 구하기
    for r in range(n):
        for c in range(r+1):
            if c ==
