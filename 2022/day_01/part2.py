import os

def highest_calories_elf(input):
    calories = list()
    carriedCalories = 0

    for current in input:
        
        if current == '\n':
            calories.append(carriedCalories)
            carriedCalories = 0
        else:
            carriedCalories += int(current.rstrip())

    calories.sort(reverse=True)
    return sum(calories[0:3])

with open(os.path.dirname(__file__) + '/input.txt') as f:
    print(highest_calories_elf(f.readlines()))