from part_1 import read_file, calculate_sum, get_first_digit, get_last_digit

digits = ["one", "two", "three", "four",
          "five", "six", "seven", "eight", "nine"]


def replace_words_with_numbers(data):
    '''replaces the words as number with numbers'''
    for index in range(len(data)):
        for i in range(9):
            data[index] = data[index].replace(
                digits[i], (digits[i][0] + str(i + 1) + digits[i][-1]))
    return data


if __name__ == '__main__':
    data = read_file('day_1/input.txt')
    data = replace_words_with_numbers(data)
    print(calculate_sum(data))  # This is the answer to the problem
