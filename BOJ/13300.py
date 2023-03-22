import sys, math
sys.stdin = open("input.txt")
# N: 학생수
# K: 한방에 최대 인원 수
N, K = map(int, input().split())
n_women = [0] * 7
n_men = [0] * 7


for _ in range(N):
    S, G = map(int, input().split())
    if S == 0:
        n_women[G] += 1
    elif S == 1:
        n_men[G] += 1
room = 0
for i in range(1, 7):

    room += math.ceil(n_women[i]/K)
    room += math.ceil(n_men[i]/K)
print(room)