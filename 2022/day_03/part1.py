import os
import string

def sum_common_items_in_rucksack(rucksacks: str):
    total_score = 0

    for rucksack in rucksacks:
        total_score += string.ascii_letters.index(get_common_item(rucksack)) + 1

    return total_score

def get_common_item (input: str):
    first_compartment = input[:len(input)//2]
    second_compartment = input[len(input)//2:]
    
    for item in first_compartment:
        if item in second_compartment:
            return item

    exit("no matches")

with open(os.path.dirname(__file__) + "/input.txt") as f:
    print(sum_common_items_in_rucksack(f.readlines()))
