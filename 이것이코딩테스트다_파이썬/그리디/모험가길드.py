#### 로직 ####
# 오름차순으로 정렬되어있다는 점에서 항상 최소한의 모험가의 수만 포함하여
# 그룹을 결성하게 되며, 따라서 최대한 많은 그룹이 구성되는 방법이다.


# 모험가 수
n = int(input())
# 공포도 리스트
lst = list(map(int, input().split()))
# 공포도를 오름차순으로 정렬
lst.sort()

group = 0
count = 0 # 현재 그룹에 포함된 모험가의 수

for i in lst:
    count += i
    if count >= n:
        group += 1
        count = 0

print(group)

