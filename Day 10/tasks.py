import unittest


def main():
    with open("Day 10/input.txt") as file:
        lines = file.readlines()


class Tests(unittest.TestCase):
    def setUp(self):
        with open("Day 10/input_test.txt") as file:
            self.lines_test = file.readlines()

    def test(self):
        pass


if __name__ == "__main__":
    unittest.main(exit=False)
    main()
