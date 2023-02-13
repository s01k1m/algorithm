import sys
sys.stdin = open("input.txt")



T = int(input())

def push(a, top, stack):
    if top < n:
        top += 1
        stack.append(a)
    elif top == n:
        print("stack is fulled")

def pop(a, top, stack):
    if len(stack) == 0:
        print("stack is empty")
    else:
        top -= 1
        stack.pop()

for tc in range(1, T+1):
    lst = list(input())
    n = len(lst)
    stack = [] # 빈 스택을 만듦
    top = 0 # 스택 push에 이용할 인덱스 초기화
    ans = 1 # 결과 일단 참이라고 가정

    for o in lst:
        if o == '(': # ( 이라면 스택에 담고
            push(o, top, stack)
            print(f'#{o} push')
        elif o == ')':
            if lst[top] == '(': # ) 이라면 그리고 지금 스택에 ( 가 담겨져 있으면 스택에서 지운다
                pop(o, top, stack)
                print(f'#{o} )')
            if top == 0: # 첫시작이 )이라면 false이므로
                ans = 0
                print(f'#{o} ')
                break
        elif o == '{': # {이면 스택에 담는다
            push(o, top, stack)
            print(f'#{o} push{')
        elif o == '}':
            if lst[top] == '{': # } 이라면 그리고 지금 스택에 { 가 담겨져 있으면 스택에서 지운다
                pop(o, top, stack)
                print(top)
            if top == 0: # 첫시작이 }이라면 false이므로
                ans = 0
                print(top)
                break
        else:
            pass
    print(stack)

    # for o in lst:
    #     if o == '(': # ( 이라면 스택에 담고
    #         push(o)
    #     elif o == ')': # ) 이라면 스택에서 지운다
    #         pop(o)
    #         if i == -1: # ) 이라서 스택에서 지우는데 irk -1이 된다면 즉 첫시작이 )이라면 false이므로
    #             ans = 0
    #             break
    #     else:
    #         pass
    #
    # # if i != 0: # 스택이 0보다 크면
    # #    ans = 0 # false이다.
    #
    # # for o in lst:
    #     if o == '{': # {이면 스택에 담는다
    #         push(o)
    #     elif o == '}': # }이면 스택에서 지운다
    #         pop(o)
    #         if i == -1: # }이라서 스택에서 지우는데 i가 -1이 된다면 즉 첫시작이 }이라면 false이므로
    #             ans = 0
    #             break
    #     else:
    #         pass

    if top != 0: # 스택이 0보다 크면
       ans = 0 # false이다.

    print(f'#{tc} {ans}')
