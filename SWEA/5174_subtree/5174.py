import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    # E: 간선의 개수
    # N: 구하고자 하는 서브 트리의 루트 노드
    E, N = map(int, input().split())
    # E로 트리 레벨을 구할 수 있다.
    level = E // 2 + 1
    left_child = [0] * (E+2)
    right_child = [0] * (E+2)

    data = list(map(int, input().split()))
    for i in range(0, E*2, 2):
        p = i
        c = i+1
        if left_child[data[p]] != 0:
            right_child[data[p]] = data[p + 1]
        else:
            left_child[data[p]] = data[p + 1]
        # if left_child[data[p]] != 0:
        #     right_child[data[p]] = data[c]
        # else:
        #     left_child[data[p]] = data[c]

    count = 0
    def cnt(node):
        global count
        count += 1
        if left_child[node]:
            cnt(left_child[node])
        if right_child[node]:
            cnt(right_child[node])

        return count

    ans = cnt(N)

    print(f'#{tc} {ans}')