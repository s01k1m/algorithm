import sys

sys.stdin = open('input.txt')

T = int(input())

# A = 49679
def counting_sort(A, k):
    print(A, len(A), max(data))
    # Data = Data 입력받은 리스트
    # Temp = Data 정렬 완료된 리스트가 될 것임

    for i in range(0, len(A)):
        C[A[i]] += 1

    for i in range(1, len(C)):
        C[i] += C[i - 1]


for to in range(1, T + 1):
    Num = int(input())
    data = list(map(int, list(input())))

    c = [0] * (max(data) + 1)

    counting_sort(data, max(data))  # 오름차순으로 정렬해줌
    print(f'#{to} {max(data)} {max(c)}')
    print(c)
