
'''




x, y = map(int, input().split())
start_x, start_y = map(int, input().split())
t = int(input())

current_x, current_y = start_x, start_y

dx = 1
dy = 1
for _ in range(t):
    if current_x == 0 or current_x == x:
        dx = -dx

    if current_y == 0 or current_y == y:
        dy = -dy

    current_x += dx
    current_y += dy

print(current_x, current_y)'''

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

a = (p + t) // w  # 증가하는 부분인지 감소하는 부분인지 확인
b = (q + t) // h  # 증가하는 부분인지 감소하는 부분인지 확인

if a % 2 == 0:  # 해당 값이 증가하는 부분이라면
    x = (p + t) % w
else:  # 해당 값이 감소하는 부분이라면
    x = w - (p + t) % w

if b % 2 == 0:  # 해당 값이 감소하는 부분이라면
    y = (q + t) % h
else:  # 해당 값이 감소하는 부분이라면
    y = h - (q + t) % h

print(x, y)