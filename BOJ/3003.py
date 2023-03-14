import sys
sys.stdin = open("input.txt")

standard = [1, 1, 2, 2, 2, 8]
mychess = list(map(int, input().split()))
result = []
for a, b in zip(standard, mychess):
    result.append(a-b)

result = map(str, result)
print(' '.join(result))
