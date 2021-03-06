def main():
    input_list = []
    with open("input.txt") as file:
        input_list = [line.strip() for line in file]

    def valid_password(low, high, letter, password):
        if password[low - 1] == letter or password[high - 1] == letter:
            if password[low - 1] == letter and password[high - 1] == letter:
                return False
            return True

        return False

    result = 0
    for entry in input_list:
        line_list = entry.split(" ")
        low_high = [int(x) for x in line_list[0].split("-")]
        letter = line_list[1][0]
        password = line_list[2]
        if valid_password(low_high[0], low_high[1], letter, password):
            result += 1

    return result


if __name__ == '__main__':
    answer = main()
    print(answer)
