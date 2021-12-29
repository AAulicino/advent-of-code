def binary_diagnostic(input):
    numberLength = (len(input[0]))
    gammaRate = ''

    for col in range(numberLength):
        ones = 0
        for line in input:
            if line[col] == '1':
                ones += 1
            else:
                ones -= 1

        gammaRate += '1' if ones >= 0 else '0'

    gammaRate = int(gammaRate, 2)
    epsilonRate = ~gammaRate & (2 ** numberLength) - 1

    return gammaRate * epsilonRate


with open('input.txt') as f:
    print(binary_diagnostic(f.read().split()))
