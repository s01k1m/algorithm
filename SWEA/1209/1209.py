#100 * 100
for i in range(10):
    time = input()
    lst = []
    for i in range(100):
        num_row = list(input().split())
        num_row = map(int, num_row)
        num_row = list(num_row)
        lst.append(num_row)
        #가로줄 더하기
    
    sum_lst = []
    # 가로줄 더하기

    for order in range(100):
        sum_r = 0
        sum_v = 0
        for number in range(100):
            sum_r = sum_r + lst[order][number]
            sum_v = sum_v + lst[number][order]
        sum_lst.append(sum_r)
        sum_lst.append(sum_v)
        sum_d = 0
        sum_d = sum_d + lst[order][order]
        sum_lst.append(sum_d)
        sum_v = 0       
        sum_v = sum_v + lst[number][100-order-1]
        sum_lst.append(sum_v)

    
    print(f'#{time} {max(sum_lst)}')
