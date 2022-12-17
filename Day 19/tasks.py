import unittest


def main():
    with open("Day 19/input.txt") as file:
        lines = list(map(str.strip, file.readlines()))


class Tests(unittest.TestCase):
    def setUp(self):
        with open("Day 19/input_test.txt") as file:
            self.lines_test = list(map(str.strip, file.readlines()))

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main(exit=False)
    main()
