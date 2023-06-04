# brute force

# 1. 기준이 될 스탠다드 문자열을 미리 만들어 놓고 비교하여 카운트한다.

# row, column
r, c = map(int, input().split())
# chess board
board = [ input() for _ in range(r)]

print(board)
answer = []
standard = ['WBWBWBWB', 'BWBWBWBW']
tmp = []


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

