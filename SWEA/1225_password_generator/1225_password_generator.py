import sys
sys.stdin = open("input.txt")


for tc in range(11):
    N = int(input()) # test 번호
    queue = list(map(int, input().split()))
    end = True
    while end:
        for i in range(1, 6):
            a = queue.pop(0) - i
            if a <= 0:
                queue.append(0)
                end = False # 와 동욱님 천재인듯
                break
            queue.append(a)

    print(f'#{tc}', end = " ")
    print(*queue)




    # int -> str으로 바꾸고
    # join문을 쓰면 된다.
