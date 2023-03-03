import sys
sys.stdin = open("input.txt")


T = int(input())        # 테스트 케이스
for tc in range(1, T+1):
    # N : 사람의 수
    # M : 걸리는 시간
    # K : M 시간이 걸렸을 때 만들 수 있는 붕어빵 수
    N, M, K = map(int, input().split())

    # 도착하는 사람의 시간 # 주의!! 정렬은 안되어있음!!!!!!!!!
사회자가 5줄로 숫자를 부르기때문에 인덱스로 사용하기 힘들어서 리스트 l에 한줄로 담