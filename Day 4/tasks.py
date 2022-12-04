import unittest


def main():
    with open("Day 4/input.txt") as file:
        assignment_pairs = file.readlines()
    print("Task 1:", count_fully_contained_assignment_pairs(assignment_pairs))
    print("Task 2:", count_overlapping_assignment_pairs(assignment_pairs))


class Assignment:
    def __init__(self, range):
        self.start = int(range.split("-")[0])
        self.end = int(range.split("-")[1])


class AssignmentPair:
    def __init__(self, line):
        self.assignments = list(map(Assignment, line.split(",")))

    def one_fully_contains_other(self):
        return ((self.assignments[0].start <= self.assignments[1].start and
                 self.assignments[0].end >= self.assignments[1].end) or
                (self.assignments[1].start <= self.assignments[0].start and
                 self.assignments[1].end >= self.assignments[0].end))

    def has_overlap(self):
        return ((self.assignments[0].end >= self.assignments[1].start and
                 self.assignments[0].start <= self.assignments[1].end) or
                (self.assignments[1].end >= self.assignments[0].start and
                self.assignments[1].start <= self.assignments[0].end))


def count_fully_contained_assignment_pairs(assignment_pair_strings):
    return len(list(filter(lambda ap: AssignmentPair(ap).one_fully_contains_other(), assignment_pair_strings)))


def count_overlapping_assignment_pairs(assignment_pair_strings):
    return len(list(filter(lambda ap: AssignmentPair(ap).has_overlap(), assignment_pair_strings)))


class Tests(unittest.TestCase):
    def setUp(self):
        with open("Day 4/input_test.txt") as file:
            self.test_assignment_pairs = file.readlines()
        with open("Day 4/input_test2.txt") as file:
            self.test_assignment_pairs2 = file.readlines()

    def test_one_fully_contains_other(self):
        self.assertEqual(False, AssignmentPair(
            "2-4,6-8").one_fully_contains_other())
        self.assertEqual(False, AssignmentPair(
            "2-7,6-8").one_fully_contains_other())
        self.assertEqual(True, AssignmentPair(
            "67-96,67-95").one_fully_contains_other())
        self.assertEqual(False, AssignmentPair(
            "2-61,1-60").one_fully_contains_other())
        self.assertEqual(True, AssignmentPair(
            "2-8,6-8").one_fully_contains_other())
        self.assertEqual(True, AssignmentPair(
            "6-8,2-8").one_fully_contains_other())
        self.assertEqual(True, AssignmentPair(
            "6-8,6-18").one_fully_contains_other())
        self.assertEqual(True, AssignmentPair(
            "6-8,6-6").one_fully_contains_other())
        self.assertEqual(True, AssignmentPair(
            "2-8,3-7").one_fully_contains_other())
        self.assertEqual(True, AssignmentPair(
            "3-7,2-8").one_fully_contains_other())

        self.assertEqual(False, AssignmentPair(
            "9-90,29-91").one_fully_contains_other())
        self.assertEqual(True, AssignmentPair(
            "72-72,25-73").one_fully_contains_other())
        self.assertEqual(True, AssignmentPair(
            "28-79,79-79").one_fully_contains_other())
        self.assertEqual(True, AssignmentPair(
            "52-77,53-53").one_fully_contains_other())
        self.assertEqual(True, AssignmentPair(
            "28-79,79-79\n").one_fully_contains_other())

    def test_count_fully_contained_assignment_pairs(self):
        self.assertEqual(2, count_fully_contained_assignment_pairs(
            self.test_assignment_pairs))
        self.assertEqual(4, count_fully_contained_assignment_pairs(
            self.test_assignment_pairs2))

    def test_has_overlap(self):
        self.assertEqual(True, AssignmentPair("5-7,7-9").has_overlap())
        self.assertEqual(False, AssignmentPair("5-7,8-9").has_overlap())
        self.assertEqual(True, AssignmentPair("5-7,5-7").has_overlap())
        self.assertEqual(True, AssignmentPair("7-7,7-7").has_overlap())
        self.assertEqual(True, AssignmentPair("7-7,7-8").has_overlap())
        self.assertEqual(False, AssignmentPair("7-17,18-18").has_overlap())
    
    def test_count_has_overlap(self):
        self.assertEqual(4, count_overlapping_assignment_pairs(
            self.test_assignment_pairs))


if __name__ == "__main__":
    unittest.main(exit=False)
    main()
