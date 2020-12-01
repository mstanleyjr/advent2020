def main():
    input_list = []
    with open("input.txt") as file:
        input_list = [int(line.strip()) for line in file if int(line.strip()) <= 2020]

    for entry in input_list:
        companion = 2020 - entry
        if companion in input_list:
            return companion * entry


if __name__ == '__main__':
    result = main()
    print(result)
