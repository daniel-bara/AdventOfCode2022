def sum_lines(lines):
    return sum(map(lambda line: int(line), lines.splitlines()))

with open("input 1.txt") as input_1_file:
    input = input_1_file.read()
    print(sum(sorted(list(map(sum_lines, input.split("\n\n"))), reverse=True)[:3]))