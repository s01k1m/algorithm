import sys
sys.stdin = open("input.txt")

# for tc in range(1, int(input())+1):
#     # N : 화덕의 크기
#     # M : 피자의 개수
#
#     N, M = map(int, input().split())
#     # cheese : 피자들의 치즈 데이터 리스트
#     cheese = list(map(int, input().split()))
#     pizza_num = [i for i in range(M)] # 피자 번호 생성
#     queue = pizza_num[0:N] # (화덕)큐 : 크기는 N인 화덕을 생성하고 (선입선출?)
#
#     while len(queue) != 1: # 화덕 안에 피자 1개만 남을때 까지
#         # 입구에 올때마다 = 인덱스가 0이 될대마다 한바퀴를 돈 것이다
#         # queue[0]에 있는 cheese를 //2 한다.
#         if cheese[queue[0]] != 0: # 아직 치즈가 다 안 녹았으면
#             cheese[queue[0]] = cheese[queue[0]] // 2 #한바퀴 돌았으므로 //2
#             queue.append(queue.pop(0)) # 맨 앞에 있는 걸 뒤로 보내기
#         else:
#             queue.pop(0)    # 치즈가 다 녹았으면  화덕에서 꺼낸다.
#             if N != M:
#                 queue.append(pizza_num[N])
#                 N += 1 # 순서대로 넣는다
#
#     print(f'#{tc} {queue[0]+1}') # 인덱스는 0부터 시작해서 피자번호를 표시하기 위해 +1 한다.

for tc in range(1, int(input()) + 1):
    #N개의 피자를 동시에 구울 수 있는 화덕
    #M개의 피자를 구워야 함
    N, M = map(int, input().split())
    temp = input().split()
    #인덱스랑 합쳐서 만들기
    pizza = [(i+1, int(temp[i])) for i in range(M)]
    #화덕에 들어갈 피자
    pizzas = pizza[:N]
    #화덕에 못들어간 피자
    pizza = pizza[N:]
    #피자가 1개남을때까지 반복
    while len(pizzas) != 1:
        #피자를 꺼내서 치즈를 반절로 줄이고
        num, cheese = pizzas.pop(0)
        cheese //=2
        #치즈가 있다면 다시 넣는다.
        if cheese: pizzas.append((num, cheese))
        #치즈가 없다면 대기중인 피자를 넣어준다,
        else :
            if pizza : pizzas.append(pizza.pop(0))
    print(f'#{tc} {pizzas.pop()[0]}')
