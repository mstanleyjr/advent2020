from utils import get_input

DAY = 3


def main(right=3, down=1):
    puzzle_input = get_input(DAY)
    puzzle_input = [list(x) for x in puzzle_input]
    x_index = 0
    y_index = 0

    trees = 0
    while y_index < len(puzzle_input):

        if puzzle_input[y_index][x_index] == "#":
            trees += 1

        x_index += right
        y_index += down

        if x_index >= len(puzzle_input[0]):
            x_index = x_index - len(puzzle_input[0])

    return trees


if __name__ == '__main__':
    slope_tests = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    result = 1
    for test in slope_tests:
        result *= main(test[0], test[1])

    print(result)
