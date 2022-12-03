import unittest


def main():
    with open("Day 3/input.txt") as file:
        rucksacks = file.readlines()
    print("Task 1:", sum_duplicate_items_per_rucksack(rucksacks))
    print("Task 2:", sum_badge_priority(rucksacks))


def make_groups(flat_list, n):
    return [flat_list[k:k+n] for k in range(0, len(flat_list), n)]


def find_common_in_3_rucksacks(rucksack_list):
    for item in rucksack_list[0]:
        if item in rucksack_list[1] and item in rucksack_list[2]:
            return item


def sum_badge_priority(rucksacks):
    return sum(map(lambda group: priority(find_common_in_3_rucksacks(group)),
                   make_groups(rucksacks, 3)))


def priority(letter):
    ascii_code = ord(letter)
    if 65 <= ascii_code <= 90:
        return ascii_code - 38
    if 97 <= ascii_code <= 122:
        return ascii_code - 96


def split_compartments(rucksack):
    half = int(len(rucksack) / 2)
    return (rucksack[:half], rucksack[half:])


def find_duplicate_in_rucksack(rucksack):
    compartment1, compartment2 = split_compartments(rucksack)
    for item in compartment1:
        if item in compartment2:
            return item


def sum_duplicate_items_per_rucksack(item_list):
    return sum(map(
        lambda rucksack: priority(find_duplicate_in_rucksack(rucksack)),
        item_list))


class Test(unittest.TestCase):
    def setUp(self) -> None:
        with open("Day 3/test_input.txt") as file:
            self.test_rucksacks = file.readlines()

    def test_priority(self):
        self.assertEqual(16, priority("p"))
        self.assertEqual(38, priority("L"))

    def test_split_compartments(self):
        self.assertEqual(
            ("jqHRNqRjqzjGDLGL", "rsFMfFZSrLrFZsSL"),
            split_compartments('jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL'))

    def test_find_common_item(self):
        self.assertEqual("p",
                         find_duplicate_in_rucksack('vJrwpWtwJgWrhcsFMMfFFhFp'))

    def test_sum_common_items(self):
        self.assertEqual(
            157, sum_duplicate_items_per_rucksack(self.test_rucksacks))

    def test_make_groups(self):
        self.assertEqual([[1, 2], [3, 4]], list(make_groups([1, 2, 3, 4], 2)))

    def test_sum_badge_priority(self):
        self.assertEqual(70, sum_badge_priority(self.test_rucksacks))


if __name__ == "__main__":
    unittest.main(exit=False)
    main()
