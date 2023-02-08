import sys

sys.stdin = open("input.txt")


# T = testcase
# n =

# LST = 문자열 데이터 *기준 행으로 나열
# LST = 문자열 데이터 *기준 열으로 나열
# N = 문자열 데이터 행(열)의 크기


def fnd_palindrome(LST, LST2, N, M):
    # 대칭인지 비교할 양 날개의 각각 길이
    num = de_num = M // 2

    for i in LST:
        for r in range(0, N - M + 1):
            num += r
            # end는 글자 반으로 가를때 오른쪽 편의 맨 첫번째인덱스임
            # 왜 따로 만들었냐면 문자열이 짝수면 딱 반으로 가랄져서 상관 없는데
            # 홀수면 중간에 문자열 기준으로 대칭이라
            # 오른쪽 편의 인덱스가 하나 뒤에서 시작해야 되서
            end = num

            if M % 2:
                end += 1

            if i[r:num] == list(reversed(i[end:end+de_num])):
                ans = i[r:end+de_num]
                return ans
            else:
                pass
            # num 초기화
            num = de_num

    for i in LST2:
        for r in range(0, N - M + 1):
            num += r
            end = num

            if M % 2:
                end += 1

            if i[r:num] == list(reversed(i[end:end+de_num])):
                ans = i[r:end+de_num]
                return ans
            else:
                pass

            num = de_num


T = int(input())

for _ in range(1, T+1):
    arr = []
    n, m = map(int, input().split())
    # 문자열을 행을 기준으로 나열하는 arr1만든다
    for i in range(n):
        row = list(input())
        arr.append(row)
    arr1 = arr
    # 열 기준으로 문자열 나열하는 arr2 만듦
    arr2 = []
    for i in range(n):
        col = []
        for j in range(n):
            col.append(arr[j][i])
        arr2.append(col)

    print(f'#{_} {"".join(fnd_palindrome(arr1, arr2, n, m))}')



