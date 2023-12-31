def read_file(file_name):
    '''file to read file with file_name as given'''
    with open(file_name) as file:
        data = file.read()
    return data.split('\n')


def create_grid(data: list[str]) -> list[list[str]]:
    '''creates a grid'''
    grid = []
    for line in data:
        new_line = []
        for char in line:
            new_line.append(char)
        grid.append(new_line)
    return grid


def get_part_numbers(grid: list[list[str]], size: int) -> list[int]:
    '''puts all the part numbers in one list'''
    part_numbers = []
    for y in range(size):
        number = ''
        symbol = False
        for x in range(size):
            if grid[y][x].isdigit() and x == (size - 1):
                number += grid[y][x]
                if not (symbol):
                    symbol = check_for_symbol(x, y, grid, symbol, size-1)
                if symbol:
                    part_numbers.append(int(number))
                symbol = False
                number = ''
            elif grid[y][x].isdigit():
                number += grid[y][x]
                if not (symbol):
                    symbol = check_for_symbol(x, y, grid, symbol, size-1)
            else:
                if symbol:
                    part_numbers.append(int(number))
                symbol = False
                number = ''
    return part_numbers


def check_for_symbol(x: int, y: int, grid: list[list[str]], symbol: bool, maximum: int) -> bool:
    '''checks if a symbol border the digit selected'''
    if x != 0 and y != 0 and not (grid[y-1][x-1] == '.' or grid[y-1][x-1].isdigit()):
        return True
    if x != 0 and not (grid[y][x-1] == '.' or grid[y][x-1].isdigit()):
        return True
    if x != 0 and y != maximum and not (grid[y+1][x-1] == '.' or grid[y+1][x-1].isdigit()):
        return True
    if y != 0 and not (grid[y-1][x] == '.' or grid[y-1][x].isdigit()):
        return True
    if y != maximum and not (grid[y+1][x] == '.' or grid[y+1][x].isdigit()):
        return True
    if x != maximum and y != 0 and not (grid[y-1][x+1] == '.' or grid[y-1][x+1].isdigit()):
        return True
    if x != maximum and not (grid[y][x+1] == '.' or grid[y][x+1].isdigit()):
        return True
    if x != maximum and y != maximum and not (grid[y+1][x+1] == '.' or grid[y+1][x+1].isdigit()):
        return True
    return False


if __name__ == "__main__":
    grid_size = len(read_file("day_3/input.txt")[0])
    data = read_file("day_3/input.txt")
    grid = create_grid(data)
    print(sum(get_part_numbers(grid, grid_size)))  # this is the solution
