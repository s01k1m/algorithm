# 농작물 수확하기 보충반 풀이

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    farm = [list(map(int, input())) for _ in range(N)]

    # 수익의 합
    crops = 0
    start = 0
    end = 0
    # 행 번호에 따라 열의 범위가 달라지므로 행 우선 탐색
    for r in range(N):  # r 번째 행이라면
        mid = N // 2
        start = end = mid
        # 중간보다 앞에 있다면, 삼각형모양
        if r < mid: # 행번호 r 만큼 중간에서 왼쪽으로 오른쪽으로 간다.
            # 왼쪽 : mid - r, start + r
            # 오른쪽 : mid + r, end - r
            crops += sum(farm[r][mid - r:mid + r])
        if r == mid: # 행번호가 가운데라면
            crops += sum(farm[r])
        if r > mid:
            # 왼쪽 : mid-(r-mid)
            # 오른쪽 : mid+(r-mid)
            crops += sum(farm[r][mid - (r-mid):mid + (r-mid)])

    print(f"#{tc} {crops}")



