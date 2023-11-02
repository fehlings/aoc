# Advent of Code 2022 Day 2
with open("2022/02_input.txt") as f:
    input = f.read()

passwords = input.split('\n')

points_1, points_2 = 0, 0
for item in passwords:
    entries = item.split(' ')
    n_min, n_max = [int(x) for x in entries[0].split('-')]

    count = 0
    for letter in entries[2]:
        if letter == entries[1][0]:
            count += 1

    if count >= n_min and count <= n_max:
        points_1 += 1

    if (entries[2][n_min-1] == entries[1][0]
            or entries[2][n_max-1] == entries[1][0])\
            and entries[2][n_min-1] != entries[2][n_max-1]:
        points_2 += 1

print("There are " + str(points_1) + " valid passwords according to rule 1")
print("There are " + str(points_2) + " valid passwords according to rule 2")
