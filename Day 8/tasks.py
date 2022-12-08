import unittest
import math


def main():
    with open("Day 8/input.txt") as file:
        lines = file.readlines()
    print("Task 1:", count_visible_trees(lines))
    print("Task 2:", get_highest_scenic_score(lines))


def rotate_coords(x, y, rotation_count, array_size):
    if rotation_count == 0:
        return x, y
    elif rotation_count == 1:
        return array_size-y-1, x
    else:
        return rotate_coords(array_size-y-1, x, rotation_count-1, array_size)


def count_visible_trees(forest_matrix):
    visibility_matrix = [
        [0 for x in range(len(forest_matrix))] for y in range(len(forest_matrix))]
    for i in range(4):
        for y_iterator in range(len(forest_matrix)):
            tallest_in_row = -1
            for x_iterator in range(len(forest_matrix)):
                x, y = x_iterator, y_iterator
                x, y = rotate_coords(
                    x_iterator, y_iterator, i, len(forest_matrix))
                if (tree := int(forest_matrix[y][x])) > tallest_in_row:
                    visibility_matrix[y][x] = 1
                    tallest_in_row = tree
    return sum(map(sum, visibility_matrix))


def get_scenic_score(x_tree, y_tree, forest_matrix):
    tree_height = forest_matrix[y_tree][x_tree]
    scores = []
    for (x_dir, y_dir) in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        direction_score = 0
        x = x_tree + x_dir
        y = y_tree + y_dir
        while x in range(len(forest_matrix)) \
                and y in range(len(forest_matrix)):
            direction_score += 1
            if (forest_matrix[y][x] >= tree_height):
                break

            x += x_dir
            y += y_dir

        scores.append(direction_score)
    return math.prod(scores)


def get_highest_scenic_score(forest_matrix):
    max = 0
    for y_iterator in range(1, len(forest_matrix)-1):
        for x_iterator in range(1, len(forest_matrix)-1):
            if (score := get_scenic_score(x_iterator, y_iterator, forest_matrix)) > max:
                max = score
    return max


class Tests(unittest.TestCase):
    def setUp(self):
        with open("Day 8/input_test.txt") as file:
            self.lines_test = list(map(str.strip, file.readlines()))
        with open("Day 8/input_test2.txt") as file:
            self.lines_test2 = list(map(str.strip, file.readlines()))
        with open("Day 8/input_test3.txt") as file:
            self.lines_test3 = list(map(str.strip, file.readlines()))

    def test_rotate_coords(self):
        self.assertEqual(rotate_coords(2, 2, 1, 3), (0, 2))
        self.assertEqual(rotate_coords(0, 2, 1, 3), (0, 0))
        self.assertEqual(rotate_coords(0, 1, 1, 3), (1, 0))
        self.assertEqual(rotate_coords(1, 1, 1, 3), (1, 1))
        self.assertEqual(rotate_coords(1, 1, 2, 3), (1, 1))
        self.assertEqual(rotate_coords(2, 2, 4, 3), (2, 2))
        self.assertEqual(rotate_coords(2, 2, 2, 3), (0, 0))

    def test_count_visible_trees(self):
        self.assertEqual(count_visible_trees(self.lines_test), 21)
        self.assertEqual(count_visible_trees(self.lines_test2), 9)
        self.assertEqual(count_visible_trees(self.lines_test3), 15)

    def test_get_scenic_score(self):
        self.assertEqual(get_scenic_score(2, 1, self.lines_test), 4)
        self.assertEqual(get_scenic_score(2, 3, self.lines_test), 8)


if __name__ == "__main__":
    unittest.main(exit=False)
    main()
