# brute force

# 1. 기준이 될 스탠다드 문자열을 미리 만들어 놓고 비교하여 카운트한다.

# row, column
r, c = map(int, input().split())
# 입력받은 chess board
board = [ input() for _ in range(r)]

answer = []
# 정석 체스 보드
standard = ['WBWBWBWB', 'BWBWBWBW']

# 체스판의 크기는 8 by 8 이므로 입력받은 보드에서 유효한 영역은 0~r-8, 0~c-8임
for i in range(0, r-7):
    for j in range(0, c-7):
        for k in range(0, 2): # (0,0)w로 시작하는 경우 b로 시작하는 경우 두번 검사
            cnt = 0
            for x in range(0, 8):
                for y in range(0, 8):

                    if board[i+x][j+y] != standard[(k+x)%2][y]: 
                        cnt += 1

            answer.append(cnt)

print(min(answer))

