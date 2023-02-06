# N = 부분집합의 원소의 갯수 a number of elements
# K = 원소의 합 required summation value
# return N개의 요소가 합이 K인 부분집합의 갯수 the number of subsets with have a sum of K and N elements
import sys
sys.stdin = open("input.txt")


A = list(range(1, 13))

T = int(input())

def find_subset(N, K):
    cnt = 0 # 카운트 리셋

    for i in range(1 << len(A)):
        subset = []
        for j in range(len(A)):
            if i & (1 << j):
                subset.append(A[j])


        if sum(subset) == K and len(subset) == N:
            cnt += 1

    return cnt


for tc in range(1, T+1):
    N, K = map(int, input().split()) # 참조  https://dojang.io/mod/page/view.php?id=2179

    print(f'#{tc} {find_subset(N, K)}')