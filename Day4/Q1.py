from utils import get_input

DAY = 4

EXPECTED_FIELDS = [
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
]

OPTIONAL_FIELDS = [
    "cid"
]


def main():
    puzzle_input = get_input(4)
    temp_list = []
    entry_list = []
    for i in range(len(puzzle_input)):
        if len(puzzle_input[i]) > 0:
            temp_list.append(puzzle_input[i])
        else:
            entry_list.append(temp_list)
            temp_list = []

    #     Then for each one gonna have to split stuff up and put it into a dataframe (I guess)
    count = 0
    for entry in entry_list:
        line_dict = {}
        valid = True
        for line in entry:
            line = line.split(" ")
            for attribute in line:
                attribute = attribute.split(":")
                if len(attribute) > 1:
                    line_dict[attribute[0]] = attribute[1]
        for field in EXPECTED_FIELDS:
            if field not in line_dict:
                valid = False

        if valid:
            count += 1

    return count


if __name__ == '__main__':
    print(main())
