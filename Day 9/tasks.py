import unittest


def main():
    with open("Day 9/input.txt") as file:
        lines = list(map(str.strip, file.readlines()))
    print("Task 1:",
          simulate_rope(
              translate_movements(lines)))
    print("Task 2:",
          simulate_long_rope(
              translate_movements(lines), 10))


def simulate_rope(movements):
    # coordinate sytem positives right, up
    head_abs = [0, 0]
    tail_rel = [0, 0]
    tail_abs = [0, 0]
    all_tail_locations = {"00": 1}
    for movement in movements:
        match movement:
            case "R":
                if tail_rel[0] == -1:
                    tail_rel = [-1, 0]
                elif tail_rel[0] > -1:
                    tail_rel[0] -= 1
                else:
                    raise Exception()
                head_abs[0] += 1
            case "U":
                if tail_rel[1] == -1:
                    tail_rel = [0, -1]
                elif tail_rel[1] > -1:
                    tail_rel[1] -= 1
                else:
                    raise Exception()
                head_abs[1] += 1
            case "L":
                if tail_rel[0] == 1:
                    tail_rel = [1, 0]
                elif tail_rel[0] < 1:
                    tail_rel[0] += 1
                else:
                    raise Exception()
                head_abs[0] -= 1
            case "D":
                if tail_rel[1] == 1:
                    tail_rel = [0, 1]
                elif tail_rel[1] < 1:
                    tail_rel[1] += 1
                else:
                    raise Exception()
                head_abs[1] -= 1
        tail_abs = [head_abs[i] + tail_rel[i] for i in range(2)]
        all_tail_locations["".join(map(str, tail_abs))] = 1
    return len(all_tail_locations)


def simulate_long_rope(movements, rope_length):
    # coordinate sytem positives right, up
    tail_abs = [[0, 0] for _ in range(rope_length)]
    all_tail_locations = {"00": 1}
    # print("---", movements)
    for command in movements:

        match command:
            case "R":
                tail_abs[0][0] += 1
            case "U":
                tail_abs[0][1] += 1
            case "L":
                tail_abs[0][0] -= 1
            case "D":
                tail_abs[0][1] -= 1
        for section in range(1, rope_length):
            s = section
            tail_rel = [tail_abs[s-1][i] - tail_abs[s][i] for i in range(2)]
            if any(tail_rel[i] < -1 or tail_rel[i] > 1 for i in range(2)):
                # move
                for i in range(2):
                    if tail_rel[i] == 0:
                        movement = 0
                    else:
                        movement = (tail_rel[i] / abs(tail_rel[i]))
                    tail_abs[s][i] = tail_abs[s][i] + movement
        # print(command, tail_abs)
        all_tail_locations["".join(map(str, tail_abs[-1]))] = 1
    return len(all_tail_locations)


def translate_movements(movement_lines):
    for line in movement_lines:
        for _ in range(int(line.split(" ")[1])):
            yield line[0]


class Tests(unittest.TestCase):
    def setUp(self):
        with open("Day 9/input_test.txt") as file:
            self.lines_test = list(map(str.strip, file.readlines()))
        with open("Day 9/input_test2.txt") as file:
            self.lines_test2 = list(map(str.strip, file.readlines()))

    def test_translate_movements(self):
        self.assertEqual(["R", "R", "U"], list(
            translate_movements(["R 2", "U 1"])))

    def test_simulate_rope(self):
        self.assertEqual(1, simulate_rope([]))
        self.assertEqual(1, simulate_rope("R"))
        self.assertEqual(1, simulate_rope("RL"))
        self.assertEqual(2, simulate_rope("RUU"))
        self.assertEqual(2, simulate_rope("RUUR"))
        self.assertEqual(13, simulate_rope(
            translate_movements(self.lines_test)))

    def test_simulate_long_rope(self):
        self.assertEqual(1, simulate_long_rope([], 2))
        self.assertEqual(1, simulate_long_rope("R", 2))
        self.assertEqual(1, simulate_long_rope("RL", 2))
        self.assertEqual(2, simulate_long_rope("RUU", 2))
        self.assertEqual(2, simulate_long_rope("RUUR", 2))
        self.assertEqual(13, simulate_long_rope(
            translate_movements(self.lines_test), 2))
        self.assertEqual(36, simulate_long_rope(
            translate_movements(self.lines_test2), 10))


if __name__ == "__main__":
    unittest.main(exit=False)
    main()
