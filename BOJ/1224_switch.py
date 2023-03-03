import sys
sys.stdin = open("input.txt")

switch_num = int(input())       # 스위치 개수
switches = list(map(int, input().split()))  # 스위치 리스트
students = int(input())         # 학생 수
for _ in range(students):       # 학생 수만큼 for 문 반복
    S, N = map(int, input().split())    # S: 성별 N: 주어지는 수
    if S == 1:      # 남학생이라면
        for i in range(N, switch_num, N):   # N 부터 N 의 배수를 i 로 
            if switches[i-1] == 0:  # [i-1] 인덱스는 0부터 시작하기 때문에 -1해야 한다. [i-1]인덱스가 0 이면
                switches[i-1] = 1   # 1로 바꿔준다
            else:                   # 1이면
                switches[i-1] = 0   # 0으로 바꿔준다.

    if S == 2:      # 여학생이라면
        for i in range(0, switch_num//2):   # 대칭 검사 시작
            # 주어진 수 N을 기준으로 좌(N-i), 우(N+i) 대칭 검사를 할 것이다.
            if 0 <= N-i-1 < switch_num and 0 <= N+i-1 < switch_num: # range 유효성 검사
                if switches[N-i-1] == switches[N+i-1]:# [N-i-1] 인덱스는 0부터 시작하기 때문에 꼭 -1을 해야한다.
                    # 대칭 자리에 있는 스위치가 서로 같으면
                    if switches[N-i-1] == 0:
                        switches[N-i-1] = switches[N+i-1] = 1
                    else:
                        switches[N-i-1] = switches[N+i-1] = 0
                else:
                    break   # 한번이라도 대칭 값이 안 맞으면 break

# 숫자 20개씩만 출력한다.
cnt = 1
for a in switches:
        cnt += 1
        print(a, end = " ")
        if cnt > 20:
            print()
            cnt = 1

# for i in range(0, N):
#     print(switches[i], end=" ")
#     if not i % 20:
#         print()