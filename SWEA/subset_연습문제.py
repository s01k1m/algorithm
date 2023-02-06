'''3
19 6 16 19 15 16 8 13 16 10
-20 -6 -13 3 -19 -9 19 -3 9 4
7 7 19 1 -18 5 -9 -11 19 18

부분집합의 합이 0이 되는 것이 존재하는지 리턴하는 함수를 작성해보자
'''


def find_subset(lst):
    n = len(lst)
    ans = 0
    # 부분집합 비트 연산으로 돌기
    for i in range(1, 1 << n):
        sub_set = []  # 부분집합 리셋, 즉 원소가 몇개 들어올지 결정
        # 이 부분부터는 갯수가 i 로 인해 갯수가 픽스되고 그 부분집합
        # 안에서 어떠한 원소가 들어올지 arr를 순회하여 for문을 돌아 부분집합을 만든다.
        for j in range(n):
            if i & (1 << j):
                sub_set.append(lst[j])

        if sum(sub_set) == 0: # 부분집합 합이 0인지 확인하고
            ans = 1 # 참이면 1 리턴

    return ans # 아니면 0 리턴



T = int(input()) # 테스트 케이스 갯수

for _ in range(1, T+1): # 테스트 케이스만큼 input 리스트 받아온 후
    divs = list(map(int, input().split()))

    print(f'#{_} {find_subset(divs)}') #결과를 프린트하기
