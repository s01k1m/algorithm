

'''
정답은 두 가지의 경우로 나뉘게 됩니다.

   2-1. c > a + b인 경우 막대기를 줄일 필요없으므로 최대 둘레의 길이가 a + b + c가 됩니다.

   2-2. 그 외의 경우 막대기 c를 적절히 줄여야 합니다. c를 a + b - 1로 줄이면 됩니다.

   따라서 답은 (a + b) * 2 - 1입니다.
'''
a, b, c = map(int, input().split())

nums = [a,b,c]
nums.sort()
arr = set(nums)
sorted(arr)

if nums[2] < nums[0] + nums[1] :
    result = 0
    for i in range(3):
        result += nums[i]
    print(result)
else:
    result = ( nums[0] + nums[1] ) * 2 - 1
    print(result)

