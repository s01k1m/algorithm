# 인덱스가 부모노드의 번호
# 배열의 값은 자식노드의 번호
# 왼쪽, 오른쪽 2개 배열을 사용

'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''

n = int(input())

left_child = [0] * (n + 1)
right_child = [0] * (n + 1)

# 간선의 개수 = 노드의 개수 - 1
e = n - 1

tree = list(map(int, input().split()))

for i in range(e):
    p = tree[i * 2]
    c = tree[i * 2 + 1]
    # 왼쪽 자식이 없으면 왼쪽에 먼저 삽입
    if left_child[p] == 0:
        left_child[p] = c
    # 왼쪽 자식이 있으면 오른쪽에 삽입
    else:
        right_child[p] = c


# 1. 전위 순회  V - L - R
def preorder(t):
    # t노드가 존재하는지 검사
    if t:
        # 데이터 처리
        print(t)
        # 왼쪽 자식 노드 탐색
        preorder(left_child[t])
        # 오른쪽 자식 노드 탐색
        preorder(right_child[t])


# 2. 중위 순회  L - V - R
def inorder(t):
    # t노드가 존재하는지 검사
    if t:
        # 왼쪽 자식 노드 탐색
        inorder(left_child[t])
        # 데이터 처리
        print(t)
        # 오른쪽 자식 노드 탐색
        inorder(right_child[t])


# 3. 후위 순회  L - R - V
def postorder(t):
    # t노드가 존재하는지 검사
    if t:
        # 왼쪽 자식 노드 탐색
        postorder(left_child[t])
        # 오른쪽 자식 노드 탐색
        postorder(right_child[t])
        # 데이터 처리
        print(t)
