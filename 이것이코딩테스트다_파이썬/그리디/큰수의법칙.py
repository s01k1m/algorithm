# N : 배열의 크기
# M : 숫자가 더해지는 횟수
# K : 특정 인덱의 수가 연속해서 더해질 수 있는 최대 횟수
# return: M번 더해서 만들 수 있느 가장 큰 합

N, M, K = map(int, input().split())
# 5, 6, 3
arr = list(map(int, input().split()))
# 6 6 6 5 6 6 6 5 6 6 6 5 6 6 6 5 6 6 5
# pattern M + 1 만큼 반복
mx_1 = max(arr)
arr.remove(mx_1)
mx_2 = max(arr)

term =  mx_1 * K + mx_2
result = (M // (K+1)) * term + (M % (K+1)) * mx_1
print(result)
