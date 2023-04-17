N = int(input())
# 기본 정렬 문제
# 100,000개 이하이므로 어떤 정렬 알고리즘을 사용해도 문제를 해결할 수 있다.

nums = []
for i in range(n):

    nums.append(int(input()))

nums.sort()

for i in nums:
    print(i, end='')