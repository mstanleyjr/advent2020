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
   result = main()
   print(result)
