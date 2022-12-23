import os
import math

KNOT_COUNT = 9


def main(input):
    rope = list()

    for _ in range(KNOT_COUNT + 1):
        rope.append((0, 0))

    visited = set()
    visited.add(rope[-1])

    motions = parse_motions(input)

    for motion in motions:
        rope[0] = move_head(rope[0], motion[0], motion[1])

        for _ in range(motion[1]):
            for knot_index in range(1, len(rope)):
                if out_of_Range(rope[knot_index - 1], rope[knot_index]):
                    rope[knot_index] = move_knot(rope[knot_index - 1], rope[knot_index])
                    visited.add(rope[-1])

    return len(visited)


def move_head(head, direction, amount):

    if direction == "R":
        return (head[0] + amount, head[1])
    if direction == "L":
        return (head[0] - amount, head[1])
    if direction == "U":
        return (head[0], head[1] + amount)
    if direction == "D":
        return (head[0], head[1] - amount)


def out_of_Range(head, tail):
    return abs(head[0] - tail[0]) > 1 or abs(head[1] - tail[1]) > 1


def move_knot(target, current):
    diff_x = target[0] - current[0]
    diff_y = target[1] - current[1]

    if diff_x != 0:
        diff_x = int(math.copysign(1, diff_x))
    if diff_y != 0:
        diff_y = int(math.copysign(1, diff_y))

    return (current[0] + diff_x, current[1] + diff_y)


def parse_motions(input) -> list[tuple[str, int]]:
    motions = list[tuple[str, int]]()

    for line in input:
        direction, amount = line.split(" ")
        motions.append((direction, int(amount)))

    return motions


with open(os.path.dirname(__file__) + "/input.txt") as f:
    print(main(tuple(map(lambda l: l.rstrip(), f.readlines()))))
