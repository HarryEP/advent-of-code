def read_file(file_name: str) -> list[str]:
    '''file to read file with file_name as given'''
    with open(file_name) as file:
        data = file.read()
    return data.split('\n')


def check_report(info: str) -> bool:
    breakdown = info.split()
    current = 0
    higher = True
    for index, level in enumerate(breakdown):
        print(index, level)
        if index == 0:
            current = int(level)
        if index == 1:
            if int(level) < current:
                higher = False
        if index != 0:
            if higher:
                if int(level) - current in [1, 2, 3]:
                    current = int(level)
                else:
                    return False
            else:
                if current - int(level) in [1, 2, 3]:
                    current = int(level)
                else:
                    return False
    return True


def count_safe(all_data: list[str]) -> int:
    '''counts the number of safe routes'''
    valids = 0
    for report in all_data:
        if check_report(report):
            valids += 1
    return valids


if __name__ == "__main__":
    data = read_file('day2/sample.txt')
    print(count_safe(data))
