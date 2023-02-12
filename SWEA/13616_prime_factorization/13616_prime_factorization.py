
T = int(input())
divs = [2, 3, 5, 7, 11] # 매번 만들어줄 필요가 없어서 함수 밖으로 뺀다

for _ in range(1, T+1):
    N = int(input())
    cnts = [0, 0, 0, 0, 0]

    for i in range(len(divs)):
        while N % divs[i] == 0:
            cnts[i] += 1
            N = N // divs[i]


    print(f'#{_}', *cnts)