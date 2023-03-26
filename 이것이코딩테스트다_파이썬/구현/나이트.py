# get the location data of a knight.
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])- int(ord('a'))) + 1

# possible directions which the knight can go.
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# check if the next step is promising
result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    # if the next step is promising, then counts will be added 1.
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_row <= 8:
        result += 1

print(result)
