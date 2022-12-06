def main():
    input_test = open("Day 6/input_test.txt").read()
    input = open("Day 6/input.txt").read()
    assert 10 == find_first_n_unique(4, input_test)
    assert 29 == find_first_n_unique(14, input_test)

    print("Task 1:", find_first_n_unique(4, input))
    print("Task 2:", find_first_n_unique(14, input))


def find_first_n_unique(n, input_string):
    for i in range(len(input_string)-n):
        substring = input_string[i:i+n]
        if len(substring) == len(dict.fromkeys(substring)):
            return i+n


if __name__ == '__main__':
    main()
