import os
import string


def sum_common_items_in_rucksack(rucksacks: str):
    total_score = 0

    i = 0

    while i < len(rucksacks):
        common = get_common_item((rucksacks[i], rucksacks[i + 1], rucksacks[i + 2]))
        total_score += string.ascii_letters.index(common) + 1
        i += 3

    return total_score


def get_common_item(sacks: tuple[str, str, str]):

    for item in sacks[0]:
        if item in sacks[1] and item in sacks[2]:
            return item

    exit("no matches")


with open(os.path.dirname(__file__) + "/input.txt") as f:
    print(sum_common_items_in_rucksack(f.readlines()))
