import sys

sys.stdin = open("input.txt")

T = int(input())
for _ in range(1, T + 1):
    a = input()
    arr = list(input().split())

    nums = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4, 'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}

    for i in nums.keys():
        for j in range(len(arr)):
            if arr[j] == i:
                arr[j] = nums[i]
    arr.sort()

    for (i, num) in enumerate(arr):
        for j in nums.keys():
            if num == nums[j]:
                arr[i] = j

    print(f'#{_} {" ".join(arr)}')

