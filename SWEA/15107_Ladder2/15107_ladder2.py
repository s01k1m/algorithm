import sys
sys.stdin = open("input.txt")

'''
outline 

tip
i was confused i and j of variables.
Thinking array is a matrix,
It will be easier to understand this,
i->y
j->x

(0,0) (0,1) (0,2)
(1,0) (1,1) (1,2)
    

variables
 T = (int) number of test case
 arr = (2 dimensional list) ladder data
 mn = size of the shortest path
 sj = x of start point (x, o)
 si = 0 # because (sj, si) is on top line of matrix
 dj = direction for next step it could be one among (1:right, -1:left, 0:down)
 cj, ci = x, y of current point (x, y) 
 cnt = counting steps
 
 

return
 ans : x of start point(x, y) with the shortest path

'''

T = 10
for test_case in range(1, T + 1):
    _ = int(input())

    arr = [[0] + list(map(int, input().split())) + [0] for _ in range(100)] # [0] is padding for right and left boundary.
    mn = 100 * 100                                      # arbitrarily designated minimum counting
    for sj in range(1, 101):
        # sj : x of start point
        si = 0
        if arr[si][sj] != 1:
            continue
        cnt, dj = 0, 0              # if you are at the top of ladder, you have to go down(dj: 0) on matter what.
        ci, cj = si, sj             # updating current position as (si, sy)
        while ci < 99:              # this fun will break when ci becomes on bottom line.
            cnt += 1
            if dj == 0:
                if arr[ci][cj-1] == 1:      # going left
                    dj = -1
                    cj -= 1
                elif arr[ci][cj+1] == 1:    # going right
                    dj = +1
                    cj += 1
                else:
                    ci += 1
            else:
                if arr[ci][cj+dj] == 1:      # going down
                    cj += dj
                else:                        # If the road is blocked on the way,
                    dj = 0
                    ci += 1
        if mn >= cnt:                # updating the shortest path
            mn, ans = cnt, sj-1
    print(f'#{test_case} {ans}')
