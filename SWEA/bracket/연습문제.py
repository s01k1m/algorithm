'''
4
()()((()))
((()((((()()((()())((())))))
(())(((())()))(()()((()))
))))


'''


T = int(input())

def push(a):
    global i
    if i < n:
        i += 1
        stack[i-1] = a

    elif i == n:
        print("stack is fulled")


def pop(a):
    global i
    global stack
    if len(stack) == 0:
        print("stack is empty")
    else:
        i -= 1
        return stack[i+1]

for tc in range(1, T+1):
    lst = list(input())
    n = len(lst)
    stack = [0] * n # 빈 스택을 만듦
    i = 0 # 스택 push에 이용할 인덱스 초기화

    for o in lst:
        if o == '(':
            push(o)
        elif o == ')':
            pop(o)
        else:
            pass

    ans = 1 # 결과 참이라고 가정
    if i != 0:
       ans = -1

    print(f'#{tc} {ans}')

