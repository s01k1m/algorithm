N, M = map(int, input().split())
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

arr3 = set(arr1+arr2)
S = len(arr3)
A = (N + M - S) # 교집합 개수
print(N+M-2*A)
