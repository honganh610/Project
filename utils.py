from random import sample

SUB_GRID_SIZE = 3
GRID_SIZE = SUB_GRID_SIZE * SUB_GRID_SIZE

def create_line_coordinates(cell_szie: int) -> list[list[tuple]]:
# Creates the x, y coordinates for drawing the grid lines
    points = []
    for y in range(1, 9):
        # horizontal
        temp = []
        temp.append((0, y * cell_szie)) # x, y points [(0, 100), (0, 200),....]
        temp.append((900, y * cell_szie)) # x, y points [(900, 100), (900, 200)...]
        points.append(temp)

    for x in range(1, 10):
        # vertical lines - from 1 to 10, to close the grid on the right side
        temp = []
        temp.append((x * cell_szie, 0))
        temp.append((x * cell_szie, 900))
        points.append(temp)
    return points


def pattern(row_num: int, col_num: int) -> int:
    return (SUB_GRID_SIZE  * (row_num % SUB_GRID_SIZE) + row_num // SUB_GRID_SIZE + col_num) % GRID_SIZE


def shuffle(samp: range) -> list:
    return sample(samp, len(samp))


def create_grid(sub_grid: int) -> list[list]:
    # Create the 9x9 grid filled with random numbers
    row_base = range(sub_grid)
    rows = [g * sub_grid + r for g in shuffle(row_base) for r in shuffle(row_base)]
    cols = [g * sub_grid + c for g in shuffle(row_base) for c in shuffle(row_base)]
    nums = shuffle(range(1, sub_grid * sub_grid + 1))
    return [[nums[pattern(r, c)] for c in cols] for r in rows]


def remove_numbers(grid: list[list], empty_cells: int) -> None:
    # Randomly sets numbers to zeros on the grids
    num_of_cells = GRID_SIZE * GRID_SIZE
    for i in sample(range(num_of_cells), empty_cells):
        grid[i // GRID_SIZE][i % GRID_SIZE] = 0