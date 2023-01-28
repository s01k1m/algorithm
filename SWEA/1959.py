time = int(input())


for i in range(time): # test case will be ten times
    n, m = map(int, input().split())
    
    n_lst = list(map(int, list(input().split()))) # make input data into int and list data
    m_lst = list(map(int, list(input().split())))
    lst = []

    if m >= n:
        '''N은 M-N만큼 뒤로 밀린 M의 요소까지 곱해질 수 있음'''
        for start in range(m-n+1):
            moving_index = start
            sum = 0
            for index_n_lst in range(n):
                num = n_lst[index_n_lst] * m_lst[moving_index] 
                moving_index += 1
                sum += num
            lst.append(sum)

    elif m < n:
        for start in range(n-m +1):
            moving_index = start
            sum = 0
            for index_m_lst in range(m):
                num = m_lst[index_m_lst] * n_lst[moving_index]
                moving_index += 1
                sum += num
            lst.append(sum)

    print(f'#{i+1} {max(lst)}')
            


