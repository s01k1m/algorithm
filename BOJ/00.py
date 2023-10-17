import sys
sys.stdin = open("input.txt")
#
# arr = [3**0, 3**1, 3**2, 3**4, 3**5]
# arr = sorted(arr, reverse=True)
# print(arr)
#광지
# num = int(input())
#
# for i in arr:
#     if (num // i) >= 1:
#         num = num - i
#
#     print(num)
# print(num)
# if num == 0:
#     print("YES")
# else:
#     print("NO")\

N = int(input()) # 숫자 개수
arr = list(map(int, input().split()))