def read_file(file_name):
    '''file to read file with file_name as given'''
    with open(file_name) as file:
        data = file.read()
    return data.split('\n')


if __name__ == "__main__":
    data = read_file('sample.txt')
