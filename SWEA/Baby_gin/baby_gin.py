'''
6자리의 숫자를 입력 받아 baby-gin 여부 찾기
완전검색 방법
1. 고려할 수 있는 모든 경우의 수 생성하기
6개의 숫자로 만들 수 있는 모든 숫자 나열(중복 포함)
2. 앞의 3자리와 두의 3자리르 자라 run 와 triplete 여부를 테스트하고 판단한다.

순열이란?

탐욕알고리즘 방법
1. 6개의 숫자는 6자리의 정수 값으로 입력됨
2. COUNTS 리스트의 각 원소를 체크하여 run과 triplete 및 Baby-gin여부를 판단함
탐욕 알고리즘 적용함.
counts 리스트에 run과 triplete가 적용되는지 확인

탐욕 알고리즘 접근의 경우, 해답을 찾아내지 못할 수 있다
1. 입력 받은 숫자를 정렬한후, 앞 뒤 3자리씩 끊어서 run 및 triplete을 확인하는 방법을 고려
{6, 4, 4, 5, 4, 4} 확인 가능
{1. 2. 3. 1. 2. 3} 정렬시 {1, 1, 2, 2, 3, 3} 로서, 오히려 baby-gin 확인을 실패할 수 있음


'''
import sys
sys.stdin = open('input.txt')
'''
baby-gin검사에 필요한 것

'''
T = int(input())
for to in range(1, T+1):
    numbers = list(map(int, list(input())))

    cnt_lst = [0] * 10 # cnt_lst[숫자] = 숫자가 몇개있는지 알려주려고 리스트를 만듦
    def CountingNum(lst):
        for i in range(0, 10): #i는 인덱스 역할을 하는 숫자로 (1, 10) 포문돌릴 것이다.
            for j in lst: # 몇개있는지 세고 싶은 대상인 J로 리스트 내에서 돌릴 것이다.

                if i == j: # j == i 이면
                    cnt_lst[i] += 1 # 인덱스 i 칸에 숫자를 +1 더해준다.

    CountingNum(numbers)
    run = 0
    tri = 0
    i = 0
    while i < 10:
        if cnt_lst[i] >= 3: # triplete 조사 후 데이터 삭제
            tri += 1
            cnt_lst[i] -= 3
            continue # 컨티뉴문 공부하기

        # run 조사 후 데이터 삭제
        if (cnt_lst[i-1] >= 1) and (cnt_lst[i] >= 1) and (cnt_lst[i+1] >= 1):
            run += 1
            cnt_lst[i - 1] -= 1
            cnt_lst[i] -= 1
            cnt_lst[i + 1] -= 1
            continue
        i += 1


    rlt = 0
    if (run + tri) == 2:
        rlt = 1

    print(f'#{to} {rlt}')



    # def CountingSort(A, B, k):
    #     #Data = Data 입력받은 리스트
    #     #Temp = Data 정렬 완료된 리스트가 될 것임
    #     #Conts = k개 요소의 리스트
    #     c = [0] * (k+1)
    #
    #     for i in range(0, len(A)):
    #         c[A[i]] += 1
    #
    #     for i in range(1, len(c)):
    #         c[i] += c[i-1]
    #
    #     for i in range( len(B)-1, -1, -1):
    #         c[A[i]] -= 1
    #         B[c[A[i]]] = A[i]
    #
    # b = [0]*len(numbers) # B를 리스트를 초기화함
    # CountingSort(numbers, b, max(numbers)) # 오름차순으로 정렬해줌
