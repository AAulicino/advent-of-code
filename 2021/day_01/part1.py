def count_larger_than_previous(input):
    previous = 0
    count = -1

    for current in input:
        if previous < current:
            count += 1
        previous = current
    return count


with open('input.txt') as f:
    print(count_larger_than_previous(map(int, f.readlines())))
