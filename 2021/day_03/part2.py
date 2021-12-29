def life_support_rating(input):

    oxygen = find_value(input, lambda x: '1' if x >= 0 else '0')
    co2 = find_value(input, lambda x: '0' if x >= 0 else '1')
    return int(oxygen, 2) * int(co2, 2)


def find_value(input, predicate):
    filteredNumbers = list(input)
    columns = len(input[0])

    for col in range(columns):
        ones = 0

        for line in filteredNumbers:
            if line[col] == '1':
                ones += 1
            else:
                ones -= 1

        filter(filteredNumbers, predicate(ones), col)

        if(len(filteredNumbers) == 1):
            break

    return filteredNumbers[0]


def filter(input, value, position):
    i = len(input) - 1
    while(i >= 0):
        if input[i][position] != value:
            input.pop(i)
        i -= 1


with open('input.txt') as f:
    print(life_support_rating(f.read().split()))
