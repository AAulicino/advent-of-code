def dive(input):
    horizontal = 0
    aim = 0
    depth = 0

    for instruction, amount in input:
        if instruction == 'forward':
            horizontal += amount
            depth += aim * amount
        elif instruction == 'up':
            aim -= amount
        else:
            aim += amount
    return horizontal * depth


with open('input.txt') as f:
    instructions = list()

    for line in f.readlines():
        tokens = line.split()
        instructions.append((tokens[0], int(tokens[1])))

print(dive(instructions))
