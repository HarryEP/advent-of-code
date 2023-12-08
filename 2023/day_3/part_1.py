def read_file(file_name):
    '''file to read file with file_name as given'''
    with open(file_name) as file:
        data = file.read()
    return data.split('\n')


def get_grid(data: list[str]) -> list[list[str]]:
    grid = []
    for line in data:
        new_line = []
        for char in line:
            new_line.append(char)
        grid.append(new_line)
    return grid


def get_part_numbers() -> list[int]:
    pass


def total_part_numbers(part_numbers: list[int]):
    pass


if __name__ == "__main__":
    print(len(read_file("day_3/sample.txt")[0]))
    data = read_file("day_3/sample.txt")
    grid = get_grid(data)
    print(grid)
