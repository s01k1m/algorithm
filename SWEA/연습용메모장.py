score_list = list(input().split()) # 점수 받아옴
#최빈수 구하기
new_score_list = {}
# 점수 set로 중복 없앤 것을 기준삼아 count하기위해 원본이랑 같이 for문 돌리기
score_set = set(score_list)
for key_score in score_set:
    count = 0
    for original_data in score_list:
        if key_score == original_data:
            count += 1

    new_score_list[key_score] = count
    sorted_score = sorted(new_score_list.items(), key = lambda x: x[1], reverse = True)
print(sorted_score[0][0])