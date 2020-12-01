# A little brute force, I think there may be a better way to do this with recursion

def main():
    input_list = []
    with open("input.txt") as file:
        input_list = [int(line.strip()) for line in file if int(line.strip()) <= 2020]

    def operand_finder(sum):
        search_list = [num for num in input_list if num <= sum]
        for item in search_list:
            companion_operand = sum - item
            if companion_operand in search_list:
                return [item, companion_operand]

        return []

    result_entries = []
    for entry in input_list:
        companion = 2020 - entry
        companions = operand_finder(companion)
        if len(companions) > 0:
            result_entries = [entry] + companions

    multiplication_result = 1
    for num in result_entries:
        multiplication_result *= num

    return multiplication_result


if __name__ == '__main__':
    result = main()
    print(result)
