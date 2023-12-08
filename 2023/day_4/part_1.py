def read_file(file_name):
    '''file to read file with file_name as given'''
    with open(file_name) as file:
        data = file.read()
    return data.split('\n')


def scratchcard_value(scratchcard: str) -> int:
    winning_numbers, card_numbers = scratchcard.split("|")
    print(winning_numbers)
    print(card_numbers)
    return 0


def sum_up_scratchcards(data: list[str]) -> int:
    total = 0
    for scratchcard in data:
        card = scratchcard.split(":")[1]
        total += scratchcard_value(card)
    return total


if __name__ == "__main__":
    data = read_file("day_4/sample.txt")
    print(sum_up_scratchcards(data))
