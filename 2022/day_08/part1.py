import os


class Vector2(object):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"({self.x},{self.y})"


def main(input):
    tree_map = parse_map(input)

    totalVisible = 0

    for row in range(len(tree_map)):
        for column in range(len(tree_map[row])):
            totalVisible += dfs_search(tree_map, Vector2(column, row))

    return totalVisible


def dfs_search(map: tuple[int, ...], current: Vector2):

    if search_dir(map, current, Vector2(1, 0)):
        return 1
    if search_dir(map, current, Vector2(-1, 0)):
        return 1
    if search_dir(map, current, Vector2(0, 1)):
        return 1
    if search_dir(map, current, Vector2(0, -1)):
        return 1

    return 0


def search_dir(tree_map: tuple[int, ...], current: Vector2, direction: Vector2):
    currentHeight = tree_map[current.y][current.x]

    curr_x = current.x + direction.x
    curr_y = current.y + direction.y
    i = 0

    while (
        curr_x >= 0
        and curr_y >= 0
        and curr_y < len(tree_map)
        and curr_x < len(tree_map[curr_y])
    ):
        if tree_map[curr_y][curr_x] >= currentHeight:
            return False

        curr_x += direction.x
        curr_y += direction.y
        i += 1

    return True


def parse_map(input) -> tuple[int, ...]:
    tree_map = list()

    for i in range(len(input)):
        tree_map.append(tuple(int(x) for x in input[i]))

    return tree_map


with open(os.path.dirname(__file__) + "/input.txt") as f:
    print(main(tuple(map(lambda l: l.rstrip(), f.readlines()))))
