import copy  

time = int(input()) # test case 몇개인지 받아오기
for case in range (time): # 테스트 시작
    n = int(input()) # N * N 정방행렬 N 받아오기
    lst = list() # 행렬 저장할 list 생성

    for data in range (n): # input으로 행마다 리스트 생성해서 lst에 넣어줌
        row = list(input().split())
        row = map(int, row)
        row = list(row)
        lst.append(row)
# 참조 https://zzozzomin08.tistory.com/20
    def matrixMult(A):
        row=len(A)
        col=len(A[0])    
        
        B = [[0 for row in range(row)]for col in range(col)]
        
        for i in range(row):
            for j in range(col):
                B[j][row-i-1]=A[i][j]

        return B
    
    rotate90 = matrixMult(lst)
    rotate180 = matrixMult(rotate90)
    rotate270 = matrixMult(rotate180)
    
#print 어떻게 해야할지 모르겠음

           
'''
    # 참조 https://www.qu3vipon.com/python-rotate-2d-array
    def rotate(input_lst):
        reverse_lst = input_lst[::-1]
        rotate_lst = list(zip(*reverse_lst))
        return rotate_lst
    

    rotate90 = rotate(lst)
    rotate180 = rotate(rotate90)
    rotate270 = rotate(rotate180)
    print(f'#{case+1}')
    for i in range(n):
        for_print = rotate90[i] + ' ' + rotate180[i] + rotate270[i]
        print(for_print)
'''    
    # new_lst = [] #회전해서 저장할 0으로 채운 N*N 행렬인 new_lst만들어줌
    # for one in range (n):
    #     line = []
    #     for two in range(n):
    #         line.append(0)
    #     new_lst.append(line)

    # #90도 회전하는 함수 만들어줌
    # def turn1():
    #     for idx1 in range(n):
    #         for idx2 in range(n):
    #             new_lst[idx2][n-idx1-1] = copy.deepcopy(lst[idx1][idx2])
            
    #     return new_lst

    # def turn2():
    #     for idx1 in range(n):
    #         for idx2 in range(n):
    #             new_lst[n-idx2-1][n-idx1-1] = copy.deepcopy(lst[idx1][idx2])
            
    #     return new_lst

    # def turn3():
    #     for idx1 in range(n):
    #         for idx2 in range(n):
    #             new_lst[n-idx2-1][idx1] = copy.deepcopy(lst[idx1][idx2])
            
    #     return new_lst

    # one_lst = turn1() #90도 회전
    # two_lst = turn2() #180도 회전
    # thr_lst = turn3() #270도 회전
    
    # print(lst, new_lst, one_lst, two_lst, thr_lst)