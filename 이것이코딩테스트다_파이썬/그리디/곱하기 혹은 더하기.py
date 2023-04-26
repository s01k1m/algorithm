# 02984
nums = input()
# 'x' '+'연산자를 넣어 결과적으로 마늗ㄹ어질 수 있는 가장 큰 수를 구하는 프로그램을 구하라.
# 단 연산은 왼쪽에서부터 순서대로 이루어진다

# 재귀로 구현할까?..음...
# + 보다 * 가 더 값을 크게 만든다.
# 현재 처리하는 숫자가 1 이하라면 더하기 연산을 수행하고,
# 그렇지 않은 경우 곱하기 연산을 수행한다.

result = int(nums[0])

for i in range(1, len(nums)):
    num = int(nums[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result += num
print(result)
