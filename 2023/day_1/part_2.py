from part_1 import read_file, calculate_sum, get_first_digit, get_last_digit

digits = ["one", "two", "three", "four",
          "five", "six", "seven", "eight", "nine"]


def replace_words_with_numbers(data):
    for index in range(len(data)):
        for i in range(9):
            data[index] = data[index].replace(digits[i], str(i + 1))
    return data


if __name__ == '__main__':
    data = read_file('day_1/sample2.txt')
    print(data)
    data = replace_words_with_numbers(data)
    print(data)
    # print(calculate_sum(data))
