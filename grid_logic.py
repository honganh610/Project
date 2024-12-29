from copy import deepcopy
from utils import create_grid, remove_numbers, SUB_GRID_SIZE, GRID_SIZE


class GridLogic:
    LEVELS = {
        'Easy': GRID_SIZE * GRID_SIZE * 3 // 7,    # 30%
        'Medium': GRID_SIZE * GRID_SIZE * 5 // 9,  # 50%
        'Hard': GRID_SIZE * GRID_SIZE * 7 // 9     # 70%
    }

    def __init__(self, level: str = 'Easy') -> None:
        if level not in self.LEVELS:
            raise ValueError(f'Invalid level: {level}')
        self.level = level
        self.grid = create_grid(SUB_GRID_SIZE)
        self.__test_grid = deepcopy(self.grid)  # create a copy of the grid before removing numbers
        remove_numbers(self.grid, self.LEVELS[self.level])
        self.occupied_cell_coordinates = self.pre_occupied_cells()


    def set_level(self, level: str) -> None:
        if level in self.LEVELS:
            self.level = level
            self.restart()
        else:
            raise ValueError(f'Invalid level: {level}')

    def restart(self) -> None:
        self.grid = create_grid(SUB_GRID_SIZE)
        self.__test_grid = deepcopy(self.grid)
        remove_numbers(self.grid, self.LEVELS[self.level])
        self.occupied_cell_coordinates = self.pre_occupied_cells()

    def check_grids(self) -> bool:
        # Check if all the cells are filled correctly
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if self.grid[y][x] != self.__test_grid[y][x]:
                    return False
        return True

    def is_cell_preoccupied(self, x: int, y: int) -> bool:
        return (y, x) in self.occupied_cell_coordinates

    def pre_occupied_cells(self) -> list[tuple]:
        occupied = []
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if self.grid[y][x] != 0:
                    occupied.append((y, x))  # (row, column)
        return occupied

    def get_cell(self, x: int, y: int) -> int:
        return self.grid[y][x]

    def set_cell(self, x: int, y: int, value: int) -> None:
        self.grid[y][x] = value


    def provide_hint(self) -> bool:
        for y in range(GRID_SIZE):
            for x in range(GRID_SIZE):
                if self.grid[y][x] == 0:
                    self.grid[y][x] = self.__test_grid[y][x]
                    return True
        return False