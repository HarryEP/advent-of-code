from part_1 import read_file, calculate_sum

digits = ["one", "two", "three", "four",
          "five", "six", "seven", "eight", "nine"]


def get_first_digit(word: str) -> str:
    '''returns first digit of the word'''

    for letter in word:
        if letter.isdigit():
            return letter
    raise ValueError(f"No digits in word {word}")


def get_last_digit(word: str) -> str:
    '''returns last digit of the word'''
    for i in range(len(word)-1, -1, -1):
        if word[i].isdigit():
            return word[i]
    raise ValueError(f"No digits in word {word}")


if __name__ == '__main__':
    data = read_file('day_1/sample.txt')
    print(calculate_sum(data))
