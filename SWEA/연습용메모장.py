A = list(range(1, 13))
print(A)

def find_subset(N, K):
    cnt = 0 # 카운트 리셋

    for i in range(1 << len(A)):
        sub_set = []
        for j in range(12):
            if i & (1 << j):
                sub_set.append(A[j])


        if sum(sub_set) == K and len(sub_set) == N:
            cnt += 1
            print(sub_set)

    return cnt

find_subset(3, 6)