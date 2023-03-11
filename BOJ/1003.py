'''T = int(input())        # T: test case

for tc in range(1, T+1):
    N = int(input())
    # return : the times that we have to use two elements,  fibonacci(0) and fibonnaci(1)
    # to figure out fibonacci(N)

    # 수열을 나열할 리스트
    f = [N]

    trying = True

    while trying:
        for index in range(len(f)):
            if f[index] > 2:
                # 1보다 큰 수열이 있다면
                f.append(f[index]-1)
                f.append(f[index]-2)
                f.remove(f[index])
            elif f[index] == 2:
                f.append(1)
                f.append(0)
                f.remove(2)


        over = False
        # 모든 리스트 요소가 2보다 작을 때
        for i in f:
            if i > 1:
                over = False
                break
            else:
                over = True

        # 종료 조건
        if over == True:
            trying = False



    cnt_0 = f.count(0)
    cnt_1 = f.count(1)

    print(cnt_0, cnt_1)


시간초과
'''

cnt0 = [1, 0]
cnt1 = [0, 1]
test_round = int(input())

for i in range(test_round):
    test = int(input())

    if test == 0:
        print("1 0")

    elif test == 1:
        print("0 1")
    else:
        for j in range(2, test_case+1):
            cnt0.append(cnt0[j-1] + cnt0[j-2])
            cnt1.append(cnt1[j-1] + cnt1[j-2])

        print(f'{cnt0.pop()} {cnt1.pop()}')
        cnt0 = [1, 0]
        cnt1 = [0, 1]
