import sys
sys.stdin = open("input.txt")

# T : 테스트 케이스
T= int(input())

# N : 한 변의 길이
# M : 플레이어가 돌을 놓는 횟수

for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 열 행, 순서로 입력되고 1부터 인덱스 시작, 컬러(0:블랙 1:화이트)
    y, x, c = map(int, input().split())
    # 돌을 놓으면 위 와래 대각선같은색 돌이 있는지 탐색하고 그 사이 있는 돌을 모두 같은색으로




    print(f'#{tc} {cnt_b} {cnt_w}')


