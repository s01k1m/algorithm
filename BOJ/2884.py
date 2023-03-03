'''
(0 ≤ H ≤ 23, 0 ≤ M ≤ 59) 
끝은 23:59
불필요한 0은 사용하지 않는다.
-45

min 0 ~ 44 -> hour -= 1 and min = 59 + min - 45
min 45 ~ 59
'''
hour, min = map(int, input().split())


if 0 <= min <= 44:
  if hour == 0:
    hour = 23
    min = 15 + min
  else:
    hour -= 1
    min = 15 + min
else:
    min -= 45

print(f'{hour} {min}')