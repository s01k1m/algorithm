#1974. 스도쿠 검증

time = int(input())

for case in range (time):
    # 스도쿠 인풋 9번 받아오기
    sudoku_lst = []
    result = 1
    for make in range (9):
    
        line = list(input().split())
        line = list(map(int, line))
        sudoku_lst.append(line)

    if result == 1:
        # 가로 확인
        for i in range(9):
            if len(set(sudoku_lst[i])) != 9:
                result=0
                break

        # 세로 확인
        for i in range(9):
            lst = []
            for j in range(9):
                lst.append(sudoku_lst[j][i])
            if len(set(lst)) != 9:
                result = 0
                break

        # 블록 확인
        for i in range(0, 9, 3):  # 시작점
            for j in range(0, 9, 3):
                # 블록
                lst = []
                for k in range(3):
                    for t in range(3):
                            lst.append(sudoku_lst[i + k][j + t])
                if len(set(lst)) != 9:
                    result = 0
                    break
                        
    print('#{} {}'.format(case+1, result))
    


    '''for make in range (9):
    
        line = list(input().split())
        line = list(map(int, line))
        sudoku_lst.append(line)

    for i in range (9):
        #i= 0, 1, 2, 3, 4,.., 9
        # 가로줄 검증
        
        if len(set(sudoku_lst[i])) != 9:
            result = 0
            print(sudoku_lst[i])
            break
        else:
            for j in range(9):
                new_set = set()
                new_set.add(sudoku_lst[j][i])
            if len(new_set) != 9:
                result = 0
                print(new_set)
                break
    for x in range(0, 9, 3): # 0 3 6
            for y in range(0, 9, 3):
                new_set2 = set() # 0 3 6
                for h in range(3):
                    for k in range(3):
                        new_set2.add(sudoku_lst[x+h][y+k])
                    if len(set(new_set2)) != 9:
                        result = 0
                        print(new_set2)
                        break
    print('#{} {}'.format(case+1, result))
'''