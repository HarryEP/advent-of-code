def read_file(file_name: str) -> list[str]:
    '''file to read file with file_name as given'''
    with open(file_name) as file:
        data = file.read()
    return data.split('\n')


def calculate_distance(values: list[str]) -> int:
    '''calculates the distance between the two values'''
    first_numbers = []
    second_numbers = []
    for pair in values:
        one, two = pair.split("   ")
        first_numbers.append(int(one))
        second_numbers.append(int(two))
    first_numbers = sorted(first_numbers)
    second_numbers = sorted(second_numbers)
    total_distance = 0
    for index, number in enumerate(first_numbers):
        total_distance += abs(second_numbers[index]-first_numbers[index])
    return total_distance


if __name__ == "__main__":
    data = read_file('day1/input_m1.txt')
    print(calculate_distance(data))
