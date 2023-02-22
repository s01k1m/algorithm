class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


A = Node("A")
B = Node("B")
C = Node("C")

# B가 A의 왼쪽 자식 노드다.
A.left = B
# C가 A의 오른쪽 자식 노드다.
A.right = C
