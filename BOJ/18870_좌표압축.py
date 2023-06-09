# [1]

num = int(input())
arr = list(map(int, input().split()))

new_arr = list(set(arr))
new_arr.sort()


'''


for i in(arr):
    print(new_arr.index(i), end=" ")

list.index(i)의 형태는 시간복잡도 O(N)을 가지고 있고 그렇다면 매번 최대 1,000,000번의 수행이 이루어지게 돼서

시간초과가 나는 것이었다.
때문에 이를 해결하기 위해 dict를 사용하기로 했다.

{ dict[요소] : 요소의 index }의 형태로 저장해 줌으로써 dict[i]의 형태로 시간복잡도 O[1]로 답을 뽑을 수 있게 하였고

문제를 통과했다.

list.index(i) 형태의 시간 복잡도 = O(N)

index[i] 형태의 시간 복잡도 = O(1)
 
    '''
dic = {new_arr[i]: i for i in range(len(new_arr))}

for i in(arr):
    print(dic[i], end=' ')

#[2]
# 더 빠른 풀이
input()
a = list(map(int,input().split()))
b = list(set(a))
b.sort()
c = {}
for i in range(len(b)):
    c[b[i]] = i
print(' '.join(str(c[i]) for i in a))