import os

CRT_WIDTH = 40
CRT_HEIGHT = 6

LIT = "#"
DARK = "."


def main(input):
    register = 1
    cycle = 0

    crt_rows = list()

    for h in range(CRT_HEIGHT):
        crt_rows.append([DARK] * CRT_WIDTH)

    for line in input:
        result = line.split()

        if result[0] == "noop":
            update_screen(crt_rows, cycle, register)
            cycle += 1

        elif result[0] == "addx":
            update_screen(crt_rows, cycle, register)
            cycle += 1

            update_screen(crt_rows, cycle, register)
            cycle += 1
            register += int(result[1])

    for line in crt_rows:
        print("".join(line))


def update_screen(crt_rows, cycle, register):

    row = int(cycle / CRT_WIDTH)
    column = cycle % CRT_WIDTH

    if abs(column - register) <= 1:
        crt_rows[row][column] = LIT
    else:
        crt_rows[row][column] = DARK


with open(os.path.dirname(__file__) + "/input.txt") as f:
    main(tuple(map(lambda l: l.rstrip(), f.readlines())))
