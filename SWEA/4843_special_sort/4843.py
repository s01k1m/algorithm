# 버블 소트로 오름차순 정렬해준다.
import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))
    
    for i in range(n-1, 0, -1):
	    for j in range(i):
		    if arr[j] > arr[j+1]:
			    arr[j], arr[j+1] = arr[j+1], arr[j]


    print(f'#{tc}', end = " ")
    for _ in range(5):
        b = arr.pop()
        s = arr.pop(0)
        print(b, end=' ')
        print(s, end=' ')
    print()


