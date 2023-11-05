# Advent of Code 2022 Day 3
with open("2022/03_input.txt") as f:
    input = f.read()

grid = [[x for x in item] for item in input.split("\n")]

slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]

total = 1

for step_column, step_row in slopes:
    count = 0
    for i in range(int(len(grid)/step_row)):
        row = i*step_row
        column = i*step_column % len(grid[0])

        if grid[row][column] == '#':
            count += 1

    print("Ouch! You hit " + str(count) + " trees!")
    total *= count

print("You hit " + str(total) + " trees in total")
