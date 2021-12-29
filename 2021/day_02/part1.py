def dive(input):
    horizontal = 0
    depth = 0

    for instruction, amount in input:
        if instruction == 'forward':
            horizontal += amount
        elif instruction == 'up':
            depth -= amount
        else:
            depth += amount
    return horizontal * depth


with open('input.txt') as f:
    instructions = list()

    for line in f.readlines():
        tokens = line.split()
        instructions.append((tokens[0], int(tokens[1])))

print(dive(instructions))
