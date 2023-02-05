T = int(input())

for _ in range(1,T+1):
    # D = 기차 사이의 거리
    # A = A 기차의 속력
    # B = B 기차의 속력
    # F = 파리의 속력
    D, A, B, F= input().split()
    
    # A와 B 기차가 만나기 까지 걸리는 시간 * 파리 속력 = 파리가 이동한 거리
    ans = (int(D) / (int(A) + int(B))) * int(F)
    print(f'#{_} {ans}')