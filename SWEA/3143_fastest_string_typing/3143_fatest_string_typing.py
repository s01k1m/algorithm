import sys
sys.stdin = open('input.txt')

T = int(input())


def fastest_string_typing(A, B):
    a = len(A)
    b = len(B)
    i = 0
    cnt = 0
    # 단어의 시작 인덱스를 i라고 한다. a -b +1을 한 자리 까지 검사하여 shortcut 이 들어갈 수 있는 자리를
    # greedy하게 탐색할 것이다.
    while i <= a - b + 1:
        # index 는 0부터 시작하므로 [i : i + b] 인덱싱한다.
        if A[i:i + b] == B:
            i += b # 일치하면 단어만큼 건너뛰어 새로 검사하도록 한다.
            cnt += 1

        else:
            i += 1

    return a - b * cnt + cnt


for tc in range(1, T + 1):
    A, B = input().split()

    print(f'#{tc} {fastest_string_typing(A, B)}')
