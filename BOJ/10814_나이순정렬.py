num = int(input())
array = []
for _ in range(num):
    age, name = input().split()
    age = int(age)
    array.append((age, name))

sorted_dict = sorted(array, key = lambda item: item[0])

for i in range(num):
    print(sorted_dict[i][0],sorted_dict[i][1])