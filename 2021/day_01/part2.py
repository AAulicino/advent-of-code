from queue import Queue


def count_larger_than_previous(input):
    queue = Queue(4)
    count = -1

    currentSum = 0
    previousSum = 0

    for current in input:

        queue.put(current)
        currentSum += current

        if queue.qsize() < 3:
            continue

        if previousSum < currentSum:
            count += 1
        previousSum = currentSum

        removed = queue.get()
        currentSum -= removed

    return count


with open('input.txt') as f:
    print(count_larger_than_previous(map(int, f.readlines())))
