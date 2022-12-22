import os


class Movement(object):
    def __init__(self, count: int, _from: int, to: int):
        self.count = count
        self._from = _from - 1
        self.to = to - 1


def move_boxes(input):

    stacks = parse_initial_setup(input)
    movements = parse_movements(input)

    apply_movements(stacks, movements)

    return "".join(map(lambda x: x[-1], stacks))


def parse_initial_setup(input: tuple[str]) -> tuple[list[str], ...]:

    stack_count = get_stack_count(input)
    stacks = tuple(list[str]() for _ in range(stack_count))

    for line in input:
        if "[" not in line:
            continue

        i = 0
        stackId = 0

        while i < len(line):
            box = line[i : i + 3]

            if "[" in box:
                stacks[stackId].insert(0, box[1])

            stackId += 1
            i += 4

    return stacks


def get_stack_count(input):
    stack_count = 0

    for line in input:
        if len(line) > 1 and line[1] == "1":
            stack_count = int(line.rstrip()[-1])

    return stack_count


def parse_movements(input: tuple[str]) -> Movement:

    movements = list()

    for line in input:
        if "move" not in line:
            continue

        tokens = line.split(" ")
        movements.append(Movement(int(tokens[1]), int(tokens[3]), int(tokens[5])))

    return movements


def apply_movements(stacks: tuple[list[str], ...], movements: tuple[Movement]):
    for movement in movements:

        origin = stacks[movement._from]
        destination = stacks[movement.to]

        for _ in range(movement.count):
            destination.append(origin[-1])
            del origin[-1]


with open(os.path.dirname(__file__) + "/input.txt") as f:
    print(move_boxes(tuple(map(lambda l: l.rstrip(), f.readlines()))))
