import sys
def electric_bus(K, N, M, charge_arr):
    '''

    :param K: 한번 충전으로 갈 수 있는 최대 정류장 수
    :param N: 종점
    :param M: 충전소의 갯수
    :param charge_arr: 충전소가 위치한 정류장 번호 array
    :return: 목표 지점에 도달했다면 최소로 충전소에 들러야 하는 횟수,
                목표 지점에 도달하지 못한다면 0을 돌려준다
    '''

    # 현재의 버스 위치와 충전 횟수를 0으로 초기화 시킵니다.
    count = 0
    cur_position = 0


    whilte True: # 밑에 코드를 무한대로 실행시키고 싶어서 와일 트루문을 썼다
        if cur_position + k >= N: #충전소에 가지 않아도 갈 수 있는 경우
            return count
        # 충전소에 들러야 하는 경우
        else:
            for charge_station in reversed(charge_arr): # 핵심 주유소를 거꾸로 검증합니다.
                if cur_position + 1 <= charge_station <= cur_position + K:
                        count += 1
                        our_position = charge_station # 버스의 위치를 재설정
                        break
            else:
                return 0

T = int(input())

for t in range(1, T+1):
    K, N, M = map(int, input().split())
    charge_arr = list(map(int, input().split()))
    print(f'#{t} {electric_bus(K, N, M, charge_arr)}')
