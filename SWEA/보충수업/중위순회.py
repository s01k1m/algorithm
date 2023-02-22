def inorder(t):
    global result
    if t:
        inorder(cleft[t])
        # 우리가 처리할 일
        # 현재 인덱스에 해당하는 알파벳을 사용해서 문자열 조립
        result += node[t]
        inorder(cright[t])


T = 10
for tc in range(1, T + 1):
    n = int(input())

    # 인덱스 <=> 알파벳 변환표
    node = [0] * (n + 1)

    cleft = [0] * (n + 1)
    cright = [0] * (n + 1)

    # 트리 만들기
    for i in range(n):
        # 노드의 정보를 한줄씩 읽어오기
        info = input().split()
        # 쪼개서 가져온다음에 글자의 개수를 세본다.
        # 0번째 => 부모노드 번호
        # 1번째 => 알파벳
        # 2번째 => 왼쪽자식 노드 번호
        # 3번째 => 오른쪽자식 노드 번호
        p = int(info[0])
        # 글자의 개수
        l = len(info)
        # 3개 이상이면 왼쪽 자식이 있음
        if l >= 3:
            cleft[p] = int(info[2])
            # 4개면 오른쪽 자식도 있음
            if l == 4:
                cright[p] = int(info[3])

        # 인덱스 p가 의미하는 알파벳을 따로 저장
        node[p] = info[1]

    result = ""
    inorder(1)
    print(f"#{tc} {result}")
