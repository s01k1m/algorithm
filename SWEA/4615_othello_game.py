import sys
sys.stdin = open("input.txt")

# T : 테스트 케이스
T= int(input())

# N : 한 변의 길이
# M : 플레이어가 돌을 놓는 횟수
N, M = map(int, input().split())

for tc in range(1, T+1):
    for