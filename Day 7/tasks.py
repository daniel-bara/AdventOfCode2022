import unittest


def main():
    with open("Day 7/input.txt") as file:
        terminal_lines = file.readlines()
    fs = build_fs(terminal_lines)
    print("Task 1:", fs.task_1_applicable_subfolders_size())
    print("Task 2:", fs.least_suitable_folder_size())


class File:
    def __init__(self, terminal_line, parent):
        self.size = int(terminal_line.split(" ")[0])
        self.name = terminal_line.split(" ")[1]
        self.parent = parent

    def get_size(self):
        return self.size


def build_fs(terminal_lines):

    root = Directory("dir /", None)
    cwd = root
    for line in map(str.strip, terminal_lines[1:]):
        if line[0] == "$":
            if line.split(" ")[1] == "ls":
                continue
            if line.split(" ")[1] == "cd":
                if line.split(" ")[2] == "..":
                    cwd = cwd.parent
                    continue
                cwd = cwd.get_child(line.split(" ")[2])
                continue
        elif line.split(" ")[0] == "dir":
            child = Directory(line, cwd)
            cwd.add_child(child)
        else:
            child = File(line, cwd)
            cwd.add_child(child)
    return root


class Directory:
    def __init__(self, terminal_line, parent):
        self.name = terminal_line.split(" ")[1]
        self.parent = parent
        self.children = {}

    def add_child(self, child_object):
        self.children[child_object.name] = child_object

    def get_child(self, child_name):
        return self.children[child_name]

    def get_size(self):
        return sum(map(lambda o: o.get_size(), self.children.values()))

    def task_1_applicable_subfolders_size(self):
        applicable_subfolders_size = sum(
            map(
                lambda d: d.task_1_applicable_subfolders_size(),
                filter(lambda c: type(c) == Directory, self.children.values())))
        if self.get_size() <= 100000:
            applicable_subfolders_size += self.get_size()
        return applicable_subfolders_size
    
    def folder_sizes(self):
        folder_sizes = []
        for subfolder in filter(lambda c: type(c) == Directory, self.children.values()):
            folder_sizes.extend(subfolder.folder_sizes())
        folder_sizes.append(self.get_size())
        return folder_sizes

    def least_suitable_folder_size(self):
        return filter(lambda s: s >= 30000000 - (70000000- self.get_size()), sorted(self.folder_sizes())).__next__()

class Tests(unittest.TestCase):
    def setUp(self):
        with open("Day 7/input_test.txt") as file:
            self.terminal_lines_test = file.readlines()
        self.fs_test = build_fs(self.terminal_lines_test)

    def test_build_fs(self):
        self.assertEqual(14848514, self.fs_test.get_child("b.txt").size)
        self.assertEqual(14848514, self.fs_test.get_child("b.txt").size)

    def test_get_size(self):
        self.assertEqual(584, self.fs_test.get_child("a").get_child("e").get_size())
        self.assertEqual(94853, self.fs_test.get_child("a").get_size())
        self.assertEqual(24933642, self.fs_test.get_child("d").get_size())
        self.assertEqual(48381165, self.fs_test.get_size())

    def test_task_1(self):
        self.assertEqual(
            95437, self.fs_test.task_1_applicable_subfolders_size())
    
    def test_task_2(self):
        self.assertEqual(
            24933642, self.fs_test.least_suitable_folder_size()
        )


if __name__ == "__main__":
    unittest.main(exit=False)
    main()
