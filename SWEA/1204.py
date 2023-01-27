'''
trial 시행횟수 = 10 입력받고
num 시행순서 = 1~10 입력받고
score_list = 100개 들어올것임

collections. Counter 안 쓰고 작성해보기
set으로 키 생성하고 value를 count하기

'''
# 데이터 받아오기
trial = int(input()) #10

for i in range (trial):
    num = int(input()) # 몇번째인지 알려주는 입력 받아옴
    score_list = list(input().split()) # 점수 받아옴
    #최빈수 구하기
    new_score_list = []
    # 점수 set로 중복 없앤 것을 기준삼아 count하기위해 원본이랑 같이 for문 돌리기
    score_set = set(score_list)
    for key_score in score_set:
        count = 0
        for original_data in score_list:
            if key_score == original_data:
                count += 1
        
        new_score_list[key_score] = count
    
    # Tuple pair로 이루어진 List로 순서 정리된 자료로 만들기
    sorted_score = sorted(new_score_list.items(), key = lambda x: x[1], reverse = True)
    
    print(f'#{num} {sorted_score[0][0]}')
    # 딕셔너리형으로 만든 {'점수': count , '점수':count, ... ... } 
    #new_score_list.append({'d':2})
    
    #print(new_score_list)

    