# 5
# 3 2 1 1 9
# 내가 생각한 로직 : 정수에서 갖고 있는 동전보다는 작지만 그 중에서 가장 큰 값부터 뺀다. 0이 될때까지 가능한 동전을 빼는데 0을 못 만들면 만들 수 없는 정수임


coinNum = int(input())
coinList = list(map(int, list(input().split())))
coinList.sort(reverse=True)

isActive = True

while isActive:
    for num in range (1, 100001):
        result = num
        # print(result, '/', num)
        
        isActive = True
        for i in coinList:
            if num >= i:
                num -= i
                # print(result, '/', num)
            
        if num :
            isActive = False
            print(result)
            break