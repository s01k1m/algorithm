import sys
sys.stdin = open("input.txt","r")


# 후위표기법으로 만들기
def make_postfix(inp):
    # inp는 input인 str


    stack = [] # 후위표기법을 만드는데 연산자를 담아줄 스택 생성
    result = ''

    for token in inp:
        if token.isdigit(): # 숫자면
            result += token # result에 바로 담아주고
        # 연산자operator이면
        else:
            if not stack : # stack이 빈값이면
                stack.append(token) #스택에 바로 넣어주고

            else:
                if token == '(': # (이면 스택에 넣어주고
                    stack.append(token)

                elif token == ')':
                    while stack[-1] != '(': # 스택이 안 비어있고 and '(' 바로 앞까지 pop한다.
                        result += stack.pop()
                    stack.pop() # (를 지우기

                elif token == '*' or token == '/':
                    while stack and (stack[-1] == "*" or stack[-1] == '/'):
                        result += stack.pop()
                    stack.append(token)

                elif token == '+' or token == '-':
                    while stack and stack[-1] != '(': # 스택이 안 비어있고 and '(' 바로 앞까지 pop한다.
                        result += stack.pop()
                    stack.append(token)

    while stack:
        result += stack.pop()



    postfix = result
    return postfix
# 후위표기법을 계산하기
def calculator(postfix):
    operator = ['*', '/', '+', '-']
    stack = [] # 피연산자를 담을 빈 stack 생성
    for i in postfix:
        if i.isdigit():
            stack.append(int(i))
        # 들어간 순서 대로 n1 n2를 계산할 것임. 따라서 n1 (operator) n2
        else:
            if i == '*':
                n2 = stack.pop() # stack에서 가장 뒤에 있던 숫자
                n1 = stack.pop() # stack에서 두번째로 뒤에 있던 숫자
                stack.append(n1 * n2)
            elif i == '+':
                n2 = stack.pop() # stack에서 가장 뒤에 있던 숫자
                n1 = stack.pop() # stack에서 두번째로 뒤에 있던 숫자
                stack.append(n1 + n2)
            elif i == '/':
                n2 = stack.pop()  # stack에서 가장 뒤에 있던 숫자
                n1 = stack.pop()  # stack에서 두번째로 뒤에 있던 숫자
                stack.append(n1 / n2)
            elif i == '-':
                n2 = stack.pop()  # stack에서 가장 뒤에 있던 숫자
                n1 = stack.pop()  # stack에서 두번째로 뒤에 있던 숫자
                stack.append(n1 - n2)

    # 다 계산하고 나면 최종 계산값이 stack[0]에 남을 것이다
    return stack[0]



T = 10

for tc in range(1, T+1):
    N = int(input())
    infix = input()
    # 후위표기법
    # 숫자 갯수 : (N-1) /2


    print(f'#{tc} {calculator(make_postfix(infix))}')


