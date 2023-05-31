# 두개 이상의 막대의 길이가 같을 때, 정삼각형
# 막대 길이가 다 다를때, (작은 2개의 막대 길이 합의 -1) + 작은 막대 2개

a, b, c = map(int, input().split())
print('$$')
arr = set([a, b, c])
sorted(arr)

if len(arr) == 2:
    result = arr[0]*3

    print(result)
elif len(arr) >= 3:
    result = arr[0] * 2 + arr[1]*2 - 1
    print(result)

