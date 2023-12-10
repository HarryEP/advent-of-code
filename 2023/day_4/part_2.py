from part_1 import read_file


def scratchcard_value(scratchcard: str, card_quantity: dict) -> int:
    '''finding scratchcard value for each scratchcard'''
    winning_numbers, card_numbers = scratchcard.split("|")
    total = 0
    for num in winning_numbers.split():
        if num in card_numbers.split():
            if total == 0:
                total = 1
            else:
                total *= 2
    return total


def sum_up_scratchcards(data: list[str]) -> int:
    '''counts the total amount of points'''
    card_quant = set_card_quantity_dictionary(len(data))
    total = 0
    for scratchcard in data:
        card = scratchcard.split(":")[1]
        total += scratchcard_value(card, card_quant)
    return total


def set_card_quantity_dictionary(num_of_cards: int) -> dict:
    '''sets the card quantity dictionary'''
    card_quantity = {}
    for i in range(1, num_of_cards+1):
        card_quantity[i] = 1
    print(card_quantity)


if __name__ == "__main__":
    data = read_file("day_4/sample.txt")
    print(sum_up_scratchcards(data))  # this is the solution printed
