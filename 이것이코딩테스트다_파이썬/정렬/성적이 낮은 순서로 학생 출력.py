num = int(input())
students = {}
for _ in range(num):
    name, age = input().split()
    students[name] = int(age)

# dict 정렬을 공부하고
dict(sorted(students.items(), key=lambda item: item[1]))
# 딕셔너리 포문 돌리면 키가 들어가네
for i in students:
    print(i, end=" ")