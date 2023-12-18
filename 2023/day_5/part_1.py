def read_file(file_name):
    '''file to read file with file_name as given'''
    with open(file_name) as file:
        data = file.read()
    return data.split('\n')


def mapping(destination: int, source: int, range_length: int):
    for i in range(source, source + range_length):
        print(i)


if __name__ == "__main__":
    # get seeds
    mapping(50, 98, 2)
