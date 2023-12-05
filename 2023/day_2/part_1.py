def read_file(file_name):
    '''file to read file with file_name as given'''
    with open(file_name) as file:
        data = file.read()
    return data.split('\n')

def is_game_valid() -> bool:
    pass

def count_valid_games(data: list[str]) -> count:
    count = 0
    for games in data
    if is_game_valid:
        count += 1

if __name__ == "__main__":
    data = read_file('sample.txt')
    print(count_valid_games(data))