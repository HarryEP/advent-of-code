def read_file(file_name: str) -> list[str]:
    '''file to read file with file_name as given'''
    with open(file_name) as file:
        data = file.read()
    return data.split('\n')


def calculate_distance(values: list[str]) -> int:
    '''calculates the distance between the two values'''
    left, right = get_lists(values)
    total_distance = 0
    for index, number in enumerate(left):
        total_distance += abs(right[index]-number)
    return total_distance


def get_lists(numbers: list[str]) -> tuple:
    'returns left and right lists in order'
    first_numbers = []
    second_numbers = []
    for pair in numbers:
        one, two = pair.split("   ")
        first_numbers.append(int(one))
        second_numbers.append(int(two))
    left = sorted(first_numbers)
    right = sorted(second_numbers)
    return left, right


if __name__ == "__main__":
    data = read_file('day1/main.txt')
    print(calculate_distance(data))
