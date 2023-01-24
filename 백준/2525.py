'''
입력 두개 받음. hour min
cooking time


time(hour, min) + cooking time = end hour , end min
cooking time은 분으로 주어짐

hour +  cooking time // 60
min + cooking time & 60

if min + cooking time >= 60
    end min = end min - 60
    hour += 1

if hour == 24:
    hour = 01
'''

hour, min = map(int, input().split())
cooking_time = int(input())

end_hour = hour + (cooking_time // 60)
end_min = min + (cooking_time % 60)

if end_min >= 60:
    end_hour += 1
    end_min -= 60

if end_hour >= 24:
    end_hour -= 24

print(end_hour, end_min)

'''
틀린 이유
1반례
22 0
120 / 24 0
정답 0 0  '''