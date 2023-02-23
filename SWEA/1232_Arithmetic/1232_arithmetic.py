import sys
sys.stdin = open("input.txt")
# https://glory-summer.tistory.com/127?category=958776
def calc(n):    # 연산을 하는 calc함수를 정의한다.
    if len(tree[n]) == 2:
        return int(tree[n][1])
    else:
        L = calc(int(tree[n][2]))
        R = calc(int(tree[n][3]))

        if tree[n][1] == '+':
            return L + R
        elif tree[n][1] == '-':
            return L - R
        elif tree[n][1] == "*":
            return L * R
        elif tree[n][1] == '/':
            return L / R




for tc in range(1, 11):
    N = int(input())
    tree = [0 for _ in range(N+1)]  # 노드의 개수+1의 0을 가진 tree 리스트를 만든다.
    for _ in range(N):              # 입력을 받으면서 노드의 번호에 해당하는 tree 위치에 입력값을 넣어준다.
        tmp = input().split()
        tree[int(tmp[0])] = tmp
    print(tree)
    print(int(tmp[0]))

    print(f'#{tc} {int(calc(1))}')

