# Advent of Code 2022 Day 1
with open("2022/01_input.txt") as f:
    data = f.read()

elves = [x.split('\n') for x in data.split('\n\n')]
calories = [sum([int(y) for y in elves[n]]) for n, x in enumerate(elves)]

solution_1 = max(calories)
print(solution_1)

solution_2 = sum(sorted(calories)[-3:])
print(solution_2)