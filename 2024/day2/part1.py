def read_file(file_name: str) -> list[str]:
    '''file to read file with file_name as given'''
    with open(file_name) as file:
        data = file.read()
    return data.split('\n')
