from part_1 import read_file, create_grid

if __name__ == "__main__":
    grid_size = len(read_file("day_3/sample.txt")[0])
    data = read_file("day_3/sample.txt")
    grid = create_grid(data)
    print(grid_size)
    print(data)
    print(grid)
