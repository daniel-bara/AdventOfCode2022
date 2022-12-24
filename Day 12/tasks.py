import unittest
import math


def main():
    with open("Day 12/input.txt") as file:
        lines = list(map(str.strip, file.readlines()))
    print("Task 1:", best_first(lines))
    print("Task 2:", reverse_best_first(lines))


def make_tile_matrix(input_matrix, reverse=False):
    def can_climb(tile, neighbor):
        if reverse:
            return tile.elevation - neighbor.elevation <= 1
        return tile.elevation - neighbor.elevation >= -1
    tile_matrix = [list(map(Tile, row)) for row in input_matrix]
    for outer_y in range(len(input_matrix)):
        for outer_x in range(len(input_matrix[0])):
            for (x, y) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                tile = tile_matrix[outer_y][outer_x]
                tile.x = outer_x
                tile.y = outer_y
                try:
                    neighbor = tile_matrix[outer_y + y][outer_x + x]
                    if (outer_x + x) in range(len(tile_matrix[0])) and (outer_y + y) in range(len(tile_matrix)) and\
                            can_climb(tile, neighbor):
                        tile.possible_next.append(neighbor)
                except:
                    pass
    return tile_matrix


def find_start(tile_matrix):
    for y in range(len(tile_matrix)):
        for x in range(len(tile_matrix[0])):
            if tile_matrix[y][x].type == "start":
                return x, y

def find_E(tile_matrix):
    for y in range(len(tile_matrix)):
        for x in range(len(tile_matrix[0])):
            if tile_matrix[y][x].type == "end":
                return x, y


def best_first(input_matrix):
    tile_matrix = make_tile_matrix(input_matrix)
    start = find_start(tile_matrix)
    start_tile = tile_matrix[start[1]][start[0]]
    backlog = [(start_tile, 0)]
    tile = start_tile
    while tile.type != "end":
        backlog.sort(key=lambda i: i[1])
        tile, cost = backlog.pop(0)
        for next_state in explore(tile, cost):
            backlog.append(next_state)
    return tile.cost


def reverse_best_first(input_matrix):
    tile_matrix = make_tile_matrix(input_matrix, reverse=True)
    start = find_E(tile_matrix)
    start_tile = tile_matrix[start[1]][start[0]]
    backlog = [(start_tile, 0)]
    tile = start_tile
    while tile.elevation != ord('a'):
        backlog.sort(key=lambda i: i[1])
        tile, cost = backlog.pop(0)
        for next_state in explore(tile, cost):
            backlog.append(next_state)
    return tile.cost


def explore(tile, cost):
    # print(tile.x, tile.y, tile.letter, cost+1)
    for neighbor in tile.possible_next:
        if cost + 1 < neighbor.cost:
            neighbor.cost = cost + 1
            yield neighbor, neighbor.cost


class Tile:
    def __init__(self, letter):
        self.letter = letter
        self.x = -1
        self.y = -1
        if letter == "S":
            self.type = "start"
            self.elevation = ord("a")
        elif letter == "E":
            self.type = "end"
            self.elevation = ord("z")
        else:
            self.type = "normal"
            self.elevation = ord(letter)
        self.possible_next = []
        self.cost = math.inf


class Tests(unittest.TestCase):
    def setUp(self):
        with open("Day 12/input_test.txt") as file:
            self.lines_test = list(map(str.strip, file.readlines()))

    def test_make_state_map(self):
        sut = make_tile_matrix(self.lines_test)
        self.assertEqual(['a', 'a', 'c', 'c'], list(
            sorted(map(lambda tile: tile.letter, sut[1][1].possible_next))))
        self.assertEqual(['c', 'e', 's', 'u'], list(
            sorted(map(lambda tile: tile.letter, sut[3][3].possible_next))))
        self.assertEqual(['a', 'c'], list(
            sorted(map(lambda tile: tile.letter, sut[0][2].possible_next))))

    def test_best_first(self):
        self.assertEqual(25, best_first(["SbcdefghijklmnopqrstuvwxyE"]))
        self.assertEqual(26, best_first([
            "Sbcdefghijklmnopqrstuvwxya",
            "zbcdefghijklmnopqrstuvwxyE"]))
        self.assertEqual(31, best_first(self.lines_test))
    def test_reverse_best_first(self):
        self.assertEqual(29, reverse_best_first(self.lines_test))


if __name__ == "__main__":
    unittest.main(exit=False)
    main()
