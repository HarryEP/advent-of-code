from part_1 import read_file


def find_min_values(game: list[str]) -> dict:
    '''finds the minimum amounts of each ball in the bag'''
    min_values = {}
    for grab in (game.split(":")[1]).split(";"):
        for handful in grab.split(","):
            amount, colour = handful.split()
            try:
                if int(amount) > min_values[colour]:
                    min_values[colour] = int(amount)
            except:
                min_values[colour] = int(amount)
    return min_values


def product_of_min_balls(game: str) -> int:
    '''gets min amount of balls and multiples them'''
    total = 1
    for value in find_min_values(game).values():
        total *= value
    return total


def sum_all_games(data: list[str]) -> int:
    '''adds all the products of min balls together'''
    total = 0
    for game in data:
        total += product_of_min_balls(game)
    return total


if __name__ == "__main__":
    data = read_file('day_2/sample1.txt')
    print(sum_all_games(data))
