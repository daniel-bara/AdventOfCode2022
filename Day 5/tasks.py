import unittest


def main():
    with open("Day 5/input.txt") as file:
        input = file.read()
        state_lines = input.split("\n\n")[0].splitlines()
        instructions = list(
            map(Instruction, input.split("\n\n")[1].splitlines()))
    print("Task 1:", read_top_items(
        execute_moving(
            read_state(state_lines),
            instructions)))
    print("Task 2:", read_top_items(
        execute_moving_preserve_order(
            read_state(state_lines),
            instructions)))


def read_state(ship_lines):
    stacks = [[] for _ in range(len(ship_lines[-1].split("   ")))]
    for i in range(len(ship_lines)-2, -1, -1):
        line = ship_lines[i]
        for j in range(len(stacks)):
            try:
                item = line[1+4*j]
            except IndexError:
                continue
            if item != " ":
                stacks[j].append(item)
    return stacks


class Instruction:
    def __init__(self, instruction_string):
        self.times = int(instruction_string.split(" ")[1])
        self.move_from = int(instruction_string.split(" ")[3])
        self.move_to = int(instruction_string.split(" ")[5])


def execute_moving(state, instructions):
    for instruction in instructions:
        for _ in range(instruction.times):
            item = state[instruction.move_from-1].pop()
            state[instruction.move_to-1].append(item)
    return state

def execute_moving_preserve_order(state, instructions):
    for instruction in instructions:
        intermediary = []
        for _ in range(instruction.times):
            item = state[instruction.move_from-1].pop()
            intermediary.append(item)
        for _ in range(instruction.times):
            item = intermediary.pop()
            state[instruction.move_to-1].append(item)
    return state


def read_top_items(state):
    return "".join(map(lambda stack: stack[-1], state))


class Tests(unittest.TestCase):
    def setUp(self):
        with open("Day 5/input_test.txt") as file:
            self.input_test = file.read()
            self.state_lines = self.input_test.split("\n\n")[0].splitlines()
            self.instructions = list(
                map(Instruction, self.input_test.split("\n\n")[1].splitlines()))

    def test_read_state(self):
        self.assertEqual([['Z', 'N'], ['M', 'C', 'D'], ['P']],
                         read_state(self.state_lines))
        self.assertEqual(4, len(self.instructions))

    def test_execute_moving(self):
        self.assertEqual([['Z', 'N'], ['M', 'C'], ['P',  'D']],
                         execute_moving([['Z', 'N'], ['M', 'C', 'D'], ['P']],
                                        [Instruction("move 1 from 2 to 3")]))

    def test_read_top_items(self):
        self.assertEqual("NCD", read_top_items(
            [['Z', 'N'], ['M', 'C'], ['P',  'D']]))


if __name__ == "__main__":
    unittest.main(exit=False)
    main()
