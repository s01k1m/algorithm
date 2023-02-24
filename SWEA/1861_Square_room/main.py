# This is a sample Python script.

# 함수 bfs 를 생성
    # [0] 생성


    # [1] 초기 데이터 삽입

    while q:
        ci, cj = q.pop(0)

        # 4 방향, 미방문, 조건 맞으면! (1차이)
        for di, dj in r((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N and v[ni][nj] ==0 and\
                abs(arr[ci][cj]- arr[ni][nj])==1:



        #for 문으로 방문 안했으면 bfs 수행하도록 한다.