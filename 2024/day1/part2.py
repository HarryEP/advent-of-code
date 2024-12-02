from part1 import get_lists, read_file


if __name__ == "__main__":
    data = read_file('day1/main.txt')
    left, right = get_lists(data)
    total = 0
    for number in left:
        total += number * right.count(number)
    print(total)
