melon = int(input())
arr = [0] * 5

s_1 = s_2 = 0 # 작은 상자 가로세로 길이
print('^0^')


for _ in range(6):
    index, length = map(int, input().split())
    if arr[index] == 0:
        arr[index] = length
    else:
        if s_1 == 0:
            s_1 = length # 작은 상자 길이 구하기
            l_1 = arr[index] + length # 큰 상자 길이 구하기
        else:
            s_2 = length # 작은 상자
            l_2 = arr[index] + length # 큰 상자 길이 구하기


big_rectangle_area = l_1 * l_2
small_rectangle_area = s_1 * s_2
area = big_rectangle_area - small_rectangle_area
print(area * melon)

        