from part_1 import read_file


def calculate_number_of_scratchcards(scratchcard: str, card_quantity: dict, card_no: int) -> dict:
    '''finding scratchcard value for each scratchcard'''
    winning_numbers, card_numbers = scratchcard.split("|")
    wins = 0
    for num in winning_numbers.split():
        if num in card_numbers.split():
            wins += 1
    for i in range(card_quantity[card_no]):
        for i in range(1, wins + 1):
            try:
                card_quantity[card_no + i] += 1
            except:
                print(f"card {card_no + i} is invalid")
    return card_quantity


def sum_up_scratchcards(data: list[str]) -> int:
    '''counts the total amount of points'''
    card_quant = set_card_quantity_dictionary(len(data))
    for i, scratchcard in enumerate(data):
        card = scratchcard.split(":")[1]
        card_quant = calculate_number_of_scratchcards(card, card_quant, i + 1)
    return sum(card_quant.values())


def set_card_quantity_dictionary(num_of_cards: int) -> dict:
    '''sets the card quantity dictionary'''
    card_quantity = {}
    for i in range(1, num_of_cards+1):
        card_quantity[i] = 1
    return card_quantity


if __name__ == "__main__":
    data = read_file("day_4/input.txt")
    print(sum_up_scratchcards(data))  # this is the solution printed
