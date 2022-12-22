import os


def redundant_assignments_count(input):
    overlap_count = 0

    for line in input:
        assignments = parse_input(line)

        if fully_overlaps(assignments[0], assignments[1]):
            overlap_count += 1

    return overlap_count


def parse_input(input: tuple[str]) -> tuple[tuple[int, ...], tuple[int, ...]]:
    entries = input.split(",")
    return ((parse_range(entries[0])), (parse_range(entries[1])))


def parse_range(input: str):
    min_max = input.split("-")
    return range(int(min_max[0]), int(min_max[1]))


def fully_overlaps(first: range, second: range):

    if first.start >= second.start and first.stop <= second.stop:
        return True

    if second.start >= first.start and second.stop <= first.stop:
        return True

    return False


with open(os.path.dirname(__file__) + "/input.txt") as f:
    print(redundant_assignments_count(f.readlines()))
