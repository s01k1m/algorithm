T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    farm = [list(map(int, input())) for _ in range(N)]

    # 수익의 합
    crops = 0

    # 탐색을 시작할 시작 인덱스
    start = 0
    # 탐색을 종료할 종료 인덱스
    end = 0
    for r in range(N):
        # 정답에 포함할 좌표 번호를 고르기
        # 행 번호에 따라 열의 범위가 달라진다.
        mid = N // 2
        start = end = mid
        # 1. 현재 행 번호가 가운데보다 작을때
        if r < mid:
            # 현재 r 번째 행의 농작물 정보는
            # 왼쪽 : mid - r , start + r
            # 오른쪽 : mid + r , end - r
            crops += sum(farm[r][mid - r:mid + r + 1])
        # 2. 현재 행 번호가 가운데번호와 같을때
        elif r == mid:
            crops += sum(farm[r])
        # 3. 현재 행 번호가 가운데보다 클때
        elif r > mid:
            crops += sum(farm[r][r - mid:N - r + mid])

    print(f"#{tc} {crops}")
