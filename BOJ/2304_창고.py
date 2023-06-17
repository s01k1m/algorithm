n = int(input()) # 기둥의 갯수
max_index, max_height = 0, 0
# 가장 높은 인덱스와 높이 찾기
array = {}

for _ in range(n):
    index, height = map(int, input().split())
    array[index] = height
    if height > max_height:
        max_index = index
        max_height = height

# 인덱스로 정렬
array = sorted(array.items())
# 시작 인덱스
last = array[-1][0]
# 마지막 인덱스
first = array[0][0]  
# 처음 높이
heights = [0] * (last+1)

for i, h in array:

    heights[i] = h

# 앞에서 부터 가장 높은 인덱스까지
temp_height = array[0][1]
result = 0

for i in range(first, max_index+1):
    if temp_height < heights[i]:
        temp_height = heights[i]
    result += temp_height

# 뒤에서 부터 가장 높은 인덱스 바로 전까지
temp_height = array[-1][1]
for i in range(last, max_index, -1):
    if temp_height < heights[i]:
        temp_height = heights[i]
    result += temp_height


print(result)