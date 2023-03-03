import sys
sys.stdin = open("input.txt")
# import copy
#내 코드

# 주사위를 쌓는 방법은 6개가 있다.
# There are six ways to stack the dice.
# 각 케이스마다 max를 이용하여 최댓값을 구한다.
# Using max, get the each max sum in every each case.
# 그 중에서 최댓값을 뽑는다.
# get the final maximum sum.

# 주사위의 숫자를 리스트로 묶으면 인덱스로 바닥과 윗면 요소를 지정할 수 있다.
# [A, B, C, D, E, F]

# 바닥과 윗면을 인덱스 짝으로 만든 딕셔너리
# bottom_and_top = {A:F, B:D, C:E, D:B, E:C, F:A}
bottom_and_top = {0:5, 1:3, 2:4, 3:1, 4:2, 5:0}
# 생각해보니 3번만 해도 될 것같다. 서로 대칭이니까





T = 1
for tc in range(1, T+1):
    N = int(input())             # 주사위 몇번 올릴 건지
    dices = [list(map(int, input().split())) for _ in range(N)]  # N개의 주사위 데이터
    sums = []
    # 인덱스를 이용해 각 요소마다 바닥면과 윗면을 없앤 new_dice 리스트를 만든다.
    for i in range(6):
        new_dice = copy.deepcopy(dices)
        sum = 0
        bottom_index = i

        # 인덱스 i를 바닥으로 가정한다.
        # 제거한다. (1)
        # i의 인덱스를 통해 윗면 인덱스의 밸류 값을 가져온다.
        # (윗면)을 제거한다. (2)
        # 이 윗면은 다시 바닥이 된다.
        # (1) (2) 반복 N-1 만큼 반복해야한다.
        for j in range(N): # j는 바닥부터 주사위의 순서라고 생각한다. 맨 바닥을 0층이라고 가정하면 N-1층 까지 있다.
            # i와 마주보고 있는 윗면 인덱스는 bottom_and_top[bottom]이다.
            top_index = bottom_and_top[bottom_index]
            top_value = dices[j][top_index]
            # i는 바닥 인덱스이다. 이 인덱스를 삭제한다.
            new_dice[j].pop(bottom_index)
            new_dice[j].remove(top_value)
            # j층의 남은 주사위 면에서 가장 최고를 뽑아 더한다.
            sum = sum + max(new_dice[j])
            if j < N-1:
                bottom_value = top_value
                bottom_index = dices[j+1].index(bottom_value)
            # print(f"index {top_index} top {top_value} ++ index {bottom_index} bottom {bottom_value}")

        sums.append(sum)

    print(max(sums))


# 재웅님 코드
case = int(input())
dice_list = list()
for _ in range(case):
    dice_list.append(list(map(int, input().split())))

dice_arrangement = {0:5, 1:3, 2:4, 3:1, 4:2, 5:0}

result = 0

# 바닥면에는 6개가 올 수 있다. (for문)
for dice_start in range(1, 7):
    # 각 케이스의 값을 저장할 변수를 선언한다.
    tmp = 0
    tmp_list = [dice[:] for dice in dice_list] # 이거 어떤 코드인가용? 또 궁금한 점 딮카피를 하는법이 궁금. 나는 내 코드에서 자꾸 얕은 복사라 오류났다.
    for dice in tmp_list: #오.... 이거 아주 좋은듯 인덱스로 찾지 말고 바로 요소를 받아오기 (별표)
        # 이전 dice에서 반환한 상단값의 index를 추출한다.
        bottom_index = dice.index(dice_start)
        top_index = dice_arrangement[bottom_index]
        # 다음 주사위를 위해 dice_start를 재설정합니다.
        dice_start = dice[top_index]
        # 아랫면과 윗면을 제외한 최대값을 케이스값에 더한다.
        dice[bottom_index] = 0
        dice[top_index] = 0
        tmp += max(dice)
    # tmp 값이 result 보다 클 경우 값을 저장해준다.
    if tmp > result:
        result = tmp
print(result)