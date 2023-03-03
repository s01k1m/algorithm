import sys
sys.stdin =open("input.txt")

arr = [list(map(int, input().split())) for _ in range(5)]
n = [list(map(int, input().split())) for _ in range(5)]
l = []
for i in range(5):
    for j in range(5):
        l.append(n[i][j])        # 사회자가 5줄로 숫자를 부르기때문에 인덱스로 사용하기 힘들어서 리스트 l에 한줄로 담음

bingo = 0
for k in range(len(l)):
    for i in range(5):
        for j in range(5):
            if l[k] == arr[i][j]:
                arr[i][j] = 'X'                 # 사회자가 리스트의 숫자를 부를때마다 cnt에 1씩 추가하고
                if all(arr[i][m] == 'X' for m in range(5)):     #행 빙고
                    bingo = bingo + 1
                if all(arr[m][j] == 'X' for m in range(5)):     #열 빙고
                    bingo = bingo + 1
                if all(arr[m][m] == 'X' for m in range(5)):     # 대각선 빙고 2개 찾을때마다 빙고에 1개씩 추가
                    bingo = bingo + 1
                if all(arr[m][4-m] == 'X' for m in range(5)):
                    bingo = bingo + 1

                if bingo >= 3:                              # 빙고 갯수가 3개 되면 cnt 출력
                    print(k + 1)
                    break