import sys
sys.stdin = open("input.txt")


def forth(list):
    ans = 0
    stack = []  # 사칙연산에 사용할 빈 스택을 만들어준다.
    operator = ['+', '-', '*', '/']
    #
    try:
        for i in list:
            if i.isdigit():         # 만약 피연산자를 만나면
                stack.append(i)     # 스택에 일단 담는다.
            else:                   # 연산자나, '.'를 만나면
                if i in operator:       # 연산 계산을 한다.
                    num_right = int(stack.pop())
                    num_left = int(stack.pop())
                    if i == '+':
                        stack.append(num_left + num_right)
                    elif i == '-':
                        stack.append(num_left - num_right)
                    elif i == '*':
                        stack.append(num_left * num_right)
                    elif i == '/':
                        stack.append(num_left // num_right)
                elif i == '.':     # 계산을 끝내고 결과를 반환 한다.
                    if len(stack) > 1:  # 제대로 된 코드는 스택 내에 정답 하나만 있어야함
                        return "error"
                    return stack[0]

    except (IndexError, ZeroDivisionError):
        return "error"



T = int(input())
for test_case in range(1, T + 1):
    postfix = list(input().split())

    print(f'#{test_case} {forth(postfix)}')
