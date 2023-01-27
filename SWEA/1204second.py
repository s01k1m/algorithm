from collections import Counter

trial = int(input()) #10
for i in range (trial):
    num = int(input()) # 몇번째인지 알려주는 입력 받아옴
    score_list = list(input().split()) # 점수 받아옴
    #최빈수 구하기
    # 점수 set로 중복 없앤 것을 기준삼아 count하기위해 원본이랑 같이 for문 돌리기
    score_with_count = Counter(score_list).most_common(1)

    print(f'#{num} {score_with_count[0][1]}')

    # Tuple pair로 이루어진 List로 순서 정리된 자료로 만들기