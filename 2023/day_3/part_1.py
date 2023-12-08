def read_file(file_name):
    '''file to read file with file_name as given'''
    with open(file_name) as file:
        data = file.read()
    return data.split('\n')


def get_part_numbers() -> list[int]:
    pass


def total_part_numbers():
    pass


if __name__ == "__main__":
    print(len(read_file("day_3/sample.txt")[0]))
