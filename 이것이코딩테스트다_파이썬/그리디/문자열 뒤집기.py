# 연속된 숫자를 뒤집을 수 있다.
# 문자열은 0, 1로 이루어짐
# return 최소 횟수 : 문자열에 있는 모든 숫자를 전부 같게 만드는

# 0001100
data = input()
# greedy 
# 연속된 숫자열 토막이 존재할때마다 그 숫자로 리스트에 넣어줄 것이다.
# 총 갯수는 == 숫자열 토막 갯수


lst0 = []
lst1 = []

def cnt(num):
    if num == 0:
        lst0.append(num)
    else:
        lst1.append(num)

cnt(int(data[0]))

for i in range(1, len(data)):
    if data[i-1] == data[i]:
        pass
    else:
        cnt(int(data[i]))

# 숫자열 토막의 갯수가 작은쪽을 뒤집으면 답이므로 작은 쪽을 출력한다
print(min(len(lst0), len(lst1)))
