import os
import math

NOOP_CYCLES = 1
ADDX_CYCLES = 2


def main(input):

    sum = get_signal_strength_at_cycle(input, 20)
    sum += get_signal_strength_at_cycle(input, 60)
    sum += get_signal_strength_at_cycle(input, 100)
    sum += get_signal_strength_at_cycle(input, 140)
    sum += get_signal_strength_at_cycle(input, 180)
    sum += get_signal_strength_at_cycle(input, 220)

    return sum


def get_signal_strength_at_cycle(input, target_cycles):
    cycles = 0
    value = 1

    for line in input:
        result = line.split()

        if cycles == target_cycles:
            break

        if result[0] == "noop":
            cycles += 1
        elif result[0] == "addx":
            cycles += 1

            if cycles == target_cycles:
                break

            cycles += 1

            if cycles == target_cycles:
                break

            value += int(result[1])

    if cycles == target_cycles:
        return cycles * value


with open(os.path.dirname(__file__) + "/input.txt") as f:
    print(main(tuple(map(lambda l: l.rstrip(), f.readlines()))))
