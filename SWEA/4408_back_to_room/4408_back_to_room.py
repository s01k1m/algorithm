import sys
sys.stdin = open("input.txt")

T = int(input())            # 테스트 케이스 수
for tc in range(1, T + 1):
    N = int(input())        # 돌아가야할 학생들의 수
    lst = [0] * 200          # 방 400개가 마주보고 있음. 복도 총 200 길이이다.

    for _ in range(N):
        room1, room2 = map(int, input().split())

        if room1 > room2:
            room1, room2 = room2, room1

        start_corridor = (room1-1)//2
        end_corridor = (room2-1)//2

        for i in range(start_corridor, end_corridor+1):
            lst[i] += 1
    sum = 0                     # 걸리는 시간

    for t in lst:
        if sum < t:
            sum = t

    print(f'#{tc} {sum}')
