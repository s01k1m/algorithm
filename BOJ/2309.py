import sys
sys.stdin = open("input.txt")

arr = [int(input()) for _ in range(9)]



s = sum(arr)

flag = True
while flag:
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j:
                if s - arr[i] - arr[j] == 100:
                    if i > j:
                        arr.pop(i)
                        arr.pop(j)
                        flag = False
                    if i < j:
                        arr.pop(j)
                        arr.pop(i)
                        flag= False
                        break
        # 내가 헷갈렸던 break 탈출하는 법
        if not flag:
            break

arr.sort()

for i in arr:
    print(i)


