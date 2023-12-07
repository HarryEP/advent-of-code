def read_file(file_name):
    '''file to read file with file_name as given'''
    with open(file_name) as file:
        data = file.read()
    return data.split('\n')


def is_round_valid(game: list[str]) -> bool:
    '''checks validity of each round within the game'''
    for handful in game:
        amount, colour = handful.split()
        if int(amount) > 12 and colour == 'red':
            return False
        elif int(amount) > 13 and colour == 'green':
            return False
        elif int(amount) > 14 and colour == 'blue':
            return False
    return True


def is_game_valid(game: str) -> bool:
    '''checks if the game in question is a valid game'''
    for grabbed_set in (game.split(":")[1]).split(";"):
        if not is_round_valid(grabbed_set.split(",")):
            return False
    return True


def count_valid_games(data: list[str]) -> int:
    '''counts all the valid games with their associated values'''
    count = 0
    for i, game in enumerate(data):
        if is_game_valid(game):
            count += (i + 1)
    return count


if __name__ == "__main__":
    data = read_file('day_2/input.txt')
    print(count_valid_games(data))  # answer printed here
