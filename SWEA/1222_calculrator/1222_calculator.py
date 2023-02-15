import sys
sys.stdin = open("input.txt","r")


# 후위표기법으로 만들기
def make_postfix(inp):
    # inp는 input인 str


    stack = [] # 후위표기법을 만드는데 연산자를 담아줄 스택 생성
    result = [] # 후위표기법을 담을 리스트 생성 # 수업에서 result!!

    for index in range(len(inp)):
        if inp[index].isdigit(): # 숫자면
            result.append(inp[index]) # result에 바로 담아주고
        else: # 연산자operator이면
            if not len(stack) : # stack이 빈값이면
                stack.append(inp[index]) #스택에 바로 넣어주고
            elif inp[index] == '(': # (이면 스택에 넣어주고
                stack.append(inp[index])
            elif inp[index] == ')':
                while stack[-1] == '(': # 스택이 안 비어있고 and '(' 바로 앞까지 pop한다.
                    result.append(stack.pop())
                stack.pop() # (를 지우기
            elif inp[index] == '+' or inp[index] == '-':
                while stack and stack[-1] != '(': # 스택이 안 비어있고 and '(' 바로 앞까지 pop한다.
                    result.append(stack.pop())
                stack.append(inp[index])
            elif inp[index] == '+' or inp[index] == '-':
                while stack and stack[-1] != '(': # 스택이 안 비어있고 and '(' 바로 앞까지 pop한다.
                    result.append(stack.pop())
                stack.append(inp[index])

    while stack:
        result += stack.pop()








    # for token in range (len(inp)):
    #     if inp[token].isdigit():  # 숫자이면
    #         postfix.append(inp[token])  # postfix에 push.
    #     else:
    #         if len(stack) == 0:
    #             stack.append(inp[token])
    #         else:
    #             if inp[token] == '(':
    #                 stack.append(inp[token])
    #             elif inp[token] == ')':
    #                 while stack[-1] != '(' or len(stack) == 0:
    #                     postfix.append(inp[token].pop())
    #                 stack.pop() # '(' pop해서 없애기
    #             elif inp[token] == '*' or inp[token] == '/':  # * , /이면
    #                 stack.append(inp[token])  # stack에 push.
    #             elif inp[token] == '+' or inp[token] == '-':  # + , - 이면
    #                 while stack and inp[-1] == '(' : # ( 나오는 스택 끝까지 다시 꺼내기
    #                     postfix.append(stack.pop())
    #                 postfix.append(stack.pop())



    postfix = result
    return postfix
# 후위표기법을 계산하기
def calculator(postfix):
    operator = ['*', '/', '+', '-']
    stack = [] # 피연산자를 담을 빈 stack 생성
    for i in postfix:
        if i.isdigit():
            stack.append(i)
        # 들어간 순서 대로 n1 n2를 계산할 것임. 따라서 n1 (operator) n2
        else:
            if i == '*':
                n2 = stack.pop() # stack에서 가장 뒤에 있던 숫자
                n1 = stack.pop() # stack에서 두번째로 뒤에 있던 숫자
                stack.append(int(n1) * int(n2))
            elif i == '+':
                n2 = stack.pop() # stack에서 가장 뒤에 있던 숫자
                n1 = stack.pop() # stack에서 두번째로 뒤에 있던 숫자
                stack.append(int(n1) + int(n2))
            elif i == '/':
                n2 = stack.pop()  # stack에서 가장 뒤에 있던 숫자
                n1 = stack.pop()  # stack에서 두번째로 뒤에 있던 숫자
                stack.append(int(n1) / int(n2))
            elif i == '-':
                n2 = stack.pop()  # stack에서 가장 뒤에 있던 숫자
                n1 = stack.pop()  # stack에서 두번째로 뒤에 있던 숫자
                stack.append(int(n1) - int(n2))

    # 다 계산하고 나면 최종 계산값이 stack[0]에 남을 것이다
    return stack[0]



T = 10

for tc in range(1, T+1):
    N = int(input())
    infix = input()
    # 후위표기법
    # 숫자 갯수 : (N-1) /2


    pf =make_postfix(infix)
    print(f'#{tc} {calculator(pf)}')


