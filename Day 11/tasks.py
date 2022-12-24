import unittest
import math


def main():
    with open("Day 11/input.txt") as file:
        input=file.read()
    print("Task 1:", task1(input))
    print("Task 2:", task2(input))


def task1(monkeys_input):
    monkey_list = list(map(Monkey1, monkeys_input.split("\n\n")))
    for i in range(20):
        for monkey in monkey_list:
            for item in monkey.process_items():
                monkey_list[item["destination"]].receive_item(item)
    return math.prod(sorted(map(lambda monkey: monkey.inspection_count,monkey_list), reverse=True)[:2])


def task2(monkeys_input, test = False):
    monkey_list = list(map(lambda line:Monkey2(line, test), monkeys_input.split("\n\n")))
    for i in range(10000):
        for monkey in monkey_list:
            # print("Monkey", monkey.number, "with items", monkey.items)
            for item in monkey.process_items():
                monkey_list[item["destination"]].receive_item(item)
                # print("Item ", item["worry_level"], "to", item["destination"])
    print(list(map(lambda monkey: monkey.inspection_count,monkey_list)))
    return math.prod(sorted(map(lambda monkey: monkey.inspection_count,monkey_list), reverse=True)[:2])

class Monkey:
    def __init__(self, init_string, test=False):
        self.test = test
        lines = init_string.splitlines()
        self.number = lines[0].split(" ")[1].split(":")[0]
        self.items = list(map(int, lines[1].split(": ")[1].split(", ")))
        self.operation = lines[2].split("new = ")[1]
        self.divisor = int(lines[3].split(" ")[-1])
        self.test_true_monkey = int(lines[4].split(" ")[-1])
        self.test_false_monkey = int(lines[5].split(" ")[-1])
        self.inspection_count = 0

    def receive_item(self, item):
        self.items.append(item["worry_level"])

    def worry_level_decrease(self, old_level):
        raise NotImplementedError()

    def process_items(self):
        for _ in range(len(self.items)):
            self.inspection_count += 1
            old = self.items.pop(0)
            new = eval(self.operation)
            new = self.worry_level_decrease(new)
            if new % self.divisor == 0:
                yield {"worry_level": new, "destination": self.test_true_monkey}
            else:
                yield {"worry_level": new, "destination": self.test_false_monkey}

class Monkey1(Monkey):
    def worry_level_decrease(self, old_level):
        return int(old_level / 3)

class Monkey2(Monkey):
    def worry_level_decrease(self, old_level):
        divisor_product = (13*17*19*23) if self.test else (2*3*5*7*11*13*17*19)
        if old_level > divisor_product:
            return old_level % divisor_product
        return old_level
        


class Tests(unittest.TestCase):
    def setUp(self):
        with open("Day 11/input_test.txt") as file:
            self.test = file.read()

    def test_process_items(self):
        sut = Monkey1(
            '''Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3''')
        items_returned = list(sut.process_items())
        self.assertEqual(items_returned, [
            {"worry_level": 500, "destination": 3},
            {"worry_level": 620, "destination": 3}])
    
    def test_task1(self):
        self.assertEqual(10605, task1(self.test))
    
    def test_task2(self):
        self.assertEqual(2713310158, task2(self.test, test=True))


if __name__ == "__main__":
    unittest.main(exit=False)
    main()
