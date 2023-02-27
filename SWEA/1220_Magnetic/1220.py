import sys
sys.stdin = open("input.txt")
# 선입선출이라 입력 파라미터 이름 queue라고 지었음
def move(queue):
    # 숫자 list string으로 바꾸기
    # join은 string
    # https://blockdmask.tistory.com/573
    queue = ''.join(str(s) for s in queue)
    print(queue)
    return queue.count('12')
    # 아래 처럼 하지 말고 걍 12세면 된다.

    # 정체된 자석 수
    # while queue:  # list가 안 비었을 동안
    #     if len(queue) == 1:     # 종료 조건
    #         return cnt
    #     elif queue.pop(0) == 1:       # 자석이 아래로 내려오는 거면
    #         if len(queue) == 0:     # 방금 팝한게 마지막 원소이면
    #             return cnt        # 종료 조건
    #         elif queue.pop(0) == 2:       # 내려오는1이랑 올라가는 2가 만났으므로 정체된 자석 +=1
    #             cnt += 1
    #             move(queue)         # 그다음 자석 검사
    #         else:
    #             move(queue)          # 다음거 검사
    #     elif queue.pop(0) == 2:      # 2위로 올라가는 거면
    #         move(queue)              # 다음 자석 검사
    # return cnt

T = 10
for tc in range(1, T+1):
    # N : 테이블의 크기
    N = int(input())

    # 1 : N극 아래(S)로 내려가야함
    # 2 : S극 위(N)로 내려가야함
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 세로줄에 놓인 자석을 탐색할 거기 때문에
    # 열로 새 리스트를 만들어 준다.
    col_list = []
    for j in range(N):
        col = []
        for i in range(N):
            if arr[i][j] != 0:          # 자석만 저장
                col.append(arr[i][j])
        col_list.append(col)

    total = 0
    for c in col_list:
        total += move(c)

    print(f'#{tc} {total}')