import os

COMMAND_CHAR = "$"
TOTAL_DISK_SPACE = 70000000
REQUIRED_FREE_SPACE = 30000000


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
    root: Directory = build_file_tree(input)

    missing_free_space = REQUIRED_FREE_SPACE - (TOTAL_DISK_SPACE - root.size)

    subdirs: list[Directory] = get_all_subdirs(root)
    subdirs.sort(key=lambda x: x.size)

    for subdir in subdirs:
        if subdir.size >= missing_free_space:
            return subdir.size

    exit("No dir found to delete")


def get_all_subdirs(input: Directory) -> list[Directory]:

    subdirs = list(input.dirs.values())

    for _dir in input.dirs.values():
        subdirs.extend(get_all_subdirs(_dir))

    return subdirs


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
