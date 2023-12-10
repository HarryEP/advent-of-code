from part_1 import read_file, create_grid


def get_gear_numbers(grid: list[list[str]], size: int) -> list[int]:
    '''puts all the gear numbers in one list'''
    gear_numbers = []
    for y in range(size):
        number = ''
        star = False
        for x in range(size):
            if grid[y][x].isdigit() and x == (size - 1):
                number += grid[y][x]
                if not star:
                    star = check_for_star(x, y, grid, star, size-1)
                if star:
                    gear_numbers.append(int(number))
                star = False
                number = ''
            elif grid[y][x].isdigit():
                number += grid[y][x]
                if not star:
                    star = check_for_star(x, y, grid, star, size-1)
            else:
                if star:
                    gear_numbers.append(int(number))
                star = False
                number = ''
    return gear_numbers


def check_for_star(x: int, y: int, grid: list[list[str]], symbol: bool, maximum: int) -> bool:
    '''checks if a star borders the digit selected'''
    if x != 0 and y != 0 and grid[y-1][x-1] == '*':
        return True
    if x != 0 and grid[y][x-1] == '*':
        return True
    if x != 0 and y != maximum and grid[y+1][x-1] == '*':
        return True
    if y != 0 and grid[y-1][x] == '*':
        return True
    if y != maximum and grid[y+1][x] == '*':
        return True
    if x != maximum and y != 0 and grid[y-1][x+1] == '*':
        return True
    if x != maximum and grid[y][x+1] == '*':
        return True
    if x != maximum and y != maximum and grid[y+1][x+1] == '*':
        return True
    return False


if __name__ == "__main__":
    grid_size = len(read_file("day_3/sample.txt")[0])
    data = read_file("day_3/sample.txt")
    grid = create_grid(data)
    print(get_gear_numbers(grid, grid_size))
