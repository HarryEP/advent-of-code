def read_file(file_name):
    '''file to read file with file_name as given'''
    with open(file_name) as file:
        data = file.read()
    return data.split('\n')


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


def calculate_sum(data: list[str]) -> int:
    total = 0
    for word in data:
        first_digit = get_first_digit(word)
        last_digit = get_last_digit(word)
        number = int(first_digit + last_digit)
        total += number
    return total


if __name__ == '__main__':
    data = read_file('day_1/sample.txt')
    print(calculate_sum(data))
