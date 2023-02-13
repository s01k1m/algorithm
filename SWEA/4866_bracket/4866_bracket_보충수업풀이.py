row = input() # 검사할 괄호 문자열

stack = []

answer = 1 # 1 > 괄호가 제대로 되어있다. 0 > 괄호가 제대로 되어있지 않다.

for c in row:
    # 1. 열린 괄호가 나온다면 stack에 push
    if c == "(":
        stack.append(c)

    # 2. 닫힌 괄호가 나온다면
    # 스택에서 pop해서 나온 괄호가 짝이 맞는지 검사
    if c == ")" or c =="}":
        if len(stack) == 0:
            answer = 0
            break

        b = stack.pop()
        if not (b =="(" and c == ")") or  (b =="{" and c == "}") :
            answer = 0
            break

# 3. 검사가 다 끝나고 나서 스택이 비어있지 않으면 잘못되어있음.
if len(stack) > 0:
    answer = 0

print(answer)