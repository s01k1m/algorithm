#가로 : 0~4 5~9 10~14 n~n+4 로 한줄씩 묶이고 이걸 
#세로 : 0,5,10,15,20 n+5
#대각선 : 0, 6, 12 , 18, 24
#대각선 : 4, 8, 12, 16, 21

num_list = list(small_text.split())
num_list = map(int, num_list)
num_list = list(num_list)
sum_list = []
#가로줄 더하기
for pattern in range(5): #range는 (행)줄의 갯수가 될 거임 여기는 5개 줄이라 5임
    sum_w = 0 
    for order in range (5): #range 열의 갯수
        sum_w = sum_w + num_list[order]
        order += 1 # 0부터 시작하겠지
    sum_list.append(sum_w)    
    pattern += 4

#세로줄 더하기
for pattern in range(5):
    sum_v = 0
    for order in range(5):
        sum_v = sum_v + num_list[pattern]
        pattern +=5
    sum_list.append(sum_v)

#대각선diagonal 더하기 대각선 2번만 돌릴것임
for pattern in [0]: #대각선 인덱스 직접 넣어줘야함 
    sum_d = 0
    for order in range(5):
        sum_d = sum_d + num_list[pattern]
        pattern += 6
    sum_list.append(sum_d)

for pattern in [24]:#대각선 인덱스 직접 넣어줘야함인덱스 가장 큰 값넣어줌
    sum_d = 0
    for order in range(5):
        sum_d = sum_d + num_list[pattern]

        pattern -= 6
    sum_list.append(sum_d)



sum_list.sort(reverse=True)
print(sum_list[0])

#두번째
for i in range(1):
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

    
print(max(sum_lst))
