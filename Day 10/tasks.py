import unittest


def main():
    with open("Day 10/input.txt") as file:
        lines = list(map(str.strip, file.readlines()))
    processor = InstructionProcessor(lines)
    sums = processor.process()
    print("\nTask 1:", sums)


class InstructionProcessor:
    def __init__(self, instruction_lines):
        self.instruction_lines = instruction_lines
        self.sum_signals = 0
        self.no_draw = False

    def process(self):
        self.sum_signals = 0
        i = 0
        x = 1
        for line in self.instruction_lines:
            if line == "noop":
                self._draw(i, x)
                i += 1
                self._check_and_update_signal_sum(i, x)
                continue
            self._draw(i, x)
            i += 1
            self._check_and_update_signal_sum(i, x)
            self._draw(i, x)
            i += 1
            self._check_and_update_signal_sum(i, x)
            x += int(line.split(" ")[1])
        return self.sum_signals

    def _draw(self, i, x):
        if self.no_draw:
            return
        if i % 40 == 0:
            print()
        if i % 40 in [x-1, x, x+1]:
            print("##", end='')
        else:
            print("..", end='')

    def _check_and_update_signal_sum(self, i, x):
        if i == 20 or (i-20) % 40 == 0:
            self.sum_signals += i * x


class Tests(unittest.TestCase):
    def setUp(self):
        with open("Day 10/input_test.txt") as file:
            self.lines_test = list(map(str.strip, file.readlines()))

    def test_process_instructions(self):
        sut = InstructionProcessor(self.lines_test)
        sut.no_draw = True
        sums = sut.process()
        self.assertEqual(sums, 11340)


if __name__ == "__main__":
    unittest.main(exit=False)
    main()
