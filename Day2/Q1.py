def main():
    input_list = []
    with open("input.txt") as file:
        input_list = [line.strip() for line in file]

    def valid_password(min, max, letter, password):
        password_list = list(password)
        count = password_list.count(letter)
        if min <= count <= max:
            return True

        return False

    result = 0
    for entry in input_list:
        line_list = entry.split(" ")
        min_max = [int(x) for x in line_list[0].split("-")]
        letter = line_list[1][0]
        password = line_list[2]
        if valid_password(min_max[0], min_max[1], letter, password):
            result += 1

    return result


if __name__ == '__main__':
    answer = main()
    print(answer)
