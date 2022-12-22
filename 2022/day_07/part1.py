import os

COMMAND_CHAR = "$"
MAX_DIR_SIZE = 100000


class File(object):
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size


class Directory(object):
    def __init__(self, name: str, parent: "Directory"):
        self.name = name
        self.parent = parent
        self.files = dict[str, File]()
        self.dirs = dict[str, "Directory"]()
        self.size = 0

    def add_dir(self, dir: "Directory"):
        self.dirs[dir.name] = dir

    def add_file(self, file: File):
        self.files[file.name] = file
        self.__increment_size(file.size)

    def __increment_size(self, size):
        self.size += size
        if self.parent:
            self.parent.__increment_size(size)


def main(input):
    root = build_file_tree(input)

    return sum_dirs_below_max_size(root, MAX_DIR_SIZE)


def sum_dirs_below_max_size(input: Directory, maxSize: int):

    size = 0

    if input.size < maxSize:
        size += input.size

    for _dir in input.dirs.values():
        size += sum_dirs_below_max_size(_dir, maxSize)

    return size


def build_file_tree(input: tuple[str]) -> Directory:

    root = Directory("/", None)
    current_dir = root

    line_index = 0

    while line_index < len(input):

        line = input[line_index]
        if line.startswith(COMMAND_CHAR):

            command = line.split(" ")

            if command[1] == "cd":

                if command[2] == "..":
                    if current_dir.parent:
                        current_dir = current_dir.parent

                elif command[2] in current_dir.dirs:
                    current_dir = current_dir.dirs[command[2]]

            elif command[1] == "ls":

                line_index += 1
                while line_index < len(input):
                    line = input[line_index]

                    if line.startswith(COMMAND_CHAR):
                        break

                    entry_info = line.split(" ")

                    if entry_info[0].startswith("dir"):
                        current_dir.add_dir(Directory(entry_info[1], current_dir))
                    else:
                        current_dir.add_file(File(entry_info[1], int(entry_info[0])))

                    line_index += 1

                continue
        line_index += 1

    return root


with open(os.path.dirname(__file__) + "/input.txt") as f:
    print(main(tuple(map(lambda l: l.rstrip(), f.readlines()))))
