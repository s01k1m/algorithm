import sys


def electric_bus(K, N, M, charge_arr):
    '''
    이 함수는 목표 지점에 도달하기 위해 필요한 최소의 충전소 갯수를 구합니다.
    만약 목표 지점에 도달할 수 없다면 0을 리턴합니다.

    :매개변수
    K (int) : 한번 충전할때마다 갈 수 있는 최대 정류장 수
    N (int) : 종점(0~N -> total (N+1)-many)
    M (int) : 충전소 갯수
    charge_arr (list) : 충전소가 있는 정류장 번호
                        (assume it has already been sorted)

    :리턴
    count (int) : 목표 지점까지 도달했을때 최소 충전횟수,
                    목표 지점을 못가는 경우 0
    '''

    # 총 버스가 가야하는 길이 : N+1
    # 결과와 현재 버스 지점을 초기화

    count = 0
    cur_position = 0 # 0으로 초기화하였음

    # 추가 충전없이 초기 상태로 갈 수 있는 정류장은
    # (cur_position + 1) ~ (cur_position + K)
    # there should be another charge station or the end point
    # we're gonna use greedy algorithm
    # since it's always better to go as far as it can without charge

    while True:
        # 만약 현재 위치에서 갈 수 있 는 거리 range 안에 종점이 있다면
        if cur_position + K >= N:
            return count # 리턴 count
        # if not
        else:
            for charge_station in reversed(charge_arr):
                if cur_position + 1 <= charge_station <= cur_position + K:
                    # 충전 없이 갈 수 있는 거리 안에 충전소가 있다면
                    count += 1
                    cur_position = charge_station
                    break
            else: # if we don't meet break in for loop
                # when impossible
                return 0

T = int(input())

for t in range(1, T+1):
    K, N, M = map(int, input().split())
    charge_arr = list(map(int, input().split()))
    print(f'#{t} {electric_bus(K, N, M, charge_arr)}')