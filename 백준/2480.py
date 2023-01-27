#입력
#3 3 6
#2 2 2
#6 2 5
'''
인풋리스트 받고

set()로 케이스 나누고
같은 눈이 3개가 나오면 10,000원+(같은 눈)×1,000원의 상금을 받게 된다. 
같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금을 받게 된다. 
모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)×100원의 상금을 받게 된다.  

프린트
'''
from collections import Counter


dice = list(input().split())
dice.sort(reverse=True)

count = Counter(dice).most_common()


if len(count) == 3:
    result = int(dice[0])*100
    print(result)
elif len(count) == 2:
    result = (int(count[0][0])*100) + 1000
    print(result)
else:
    result = (int(count[0][0])*1000) + 10000
    print(result)