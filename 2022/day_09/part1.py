import os
import math


def main(input):
    head = (0, 0)
    tail = (0, 0)

    visited = set()
    visited.add(tail)

    motions = parse_motions(input)

    for motion in motions:
        head = move_head(head, motion[0], motion[1])

        while head_out_of_Range(head, tail):
            tail = move_tail(head, tail)
            visited.add(tail)

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


def head_out_of_Range(head, tail):
    return abs(head[0] - tail[0]) > 1 or abs(head[1] - tail[1]) > 1


def move_tail(head, tail):
    diff_x = head[0] - tail[0]
    diff_y = head[1] - tail[1]

    if diff_x != 0:
        diff_x = int(math.copysign(1, diff_x))
    if diff_y != 0:
        diff_y = int(math.copysign(1, diff_y))

    return (tail[0] + diff_x, tail[1] + diff_y)


def parse_motions(input) -> list[tuple[str, int]]:
    motions = list[tuple[str, int]]()

    for line in input:
        direction, amount = line.split(" ")
        motions.append((direction, int(amount)))

    return motions


with open(os.path.dirname(__file__) + "/input.txt") as f:
    print(main(tuple(map(lambda l: l.rstrip(), f.readlines()))))
