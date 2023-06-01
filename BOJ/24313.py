a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

result = True
for n in range(0, c+1):
    if a1 * n + a0 > c * n:
        result = False

if result == False:
    print(0)
else:
    print(1)