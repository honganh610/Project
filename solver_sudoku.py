class SolveSudoku:
    def __init__(self, grid_size=9, sub_grize_size=3):
        self.grid_size = grid_size
        self.sub_grid_size = sub_grize_size
        self.grid = [
                     [0 for _ in range(grid_size)]
                     for _ in range(grid_size)
        ]

    def set_cell(self, row, col, value):
        '''Set a value at a specific position'''
        self.grid[row][col] = value

    def reset_grid(self):
        '''Reset the grid to empty'''
        self.grid = [
                     [0 for _ in range(self.grid_size)]
                     for _ in range(self.grid_size)
        ]

    def solve(self):
        '''Solve the Sudoku puzzle using backtracking.'''
        empty = self.find_empty_cell()
        if not empty:
            return True

        row, col = empty
        for num in range(1, self.grid_size + 1):
            if self.is_valid(num, row, col):
                self.grid[row][col] = num
                if self.solve():
                    return True
                self.grid[row][col] = 0
        return False

    def find_empty_cell(self):
        '''Find the first empty cell in the grid'''
        for row in range(self.grid_size):
            for col in range(self.grid_size):
                if self.grid[row][col] == 0:
                    return row, col
        return None

    def is_valid(self, num, row, col):
        '''Check if placing 'num' at (row, col) is valid'''
        if num in self.grid[row]:
            return False
        if num in [self.grid[r][col] for r in range(self.grid_size)]:
            return False

        sub_grid_row = (row // self.sub_grid_size) * self.sub_grid_size
        sub_grid_col = (col // self.sub_grid_size) * self.sub_grid_size
        for r in range(sub_grid_row, sub_grid_row + self.sub_grid_size):
            for c in range(sub_grid_col, sub_grid_col + self.sub_grid_size):
                if self.grid[r][c] == num:
                    return False
        return True

    def is_valid_grid(self):
        for row in range(self.grid_size):
            for col in range(self.grid_size):
                num = self.grid[row][col]
                if num != 0:
                    self.grid[row][col] = 0
                    if not self.is_valid(num, row, col):
                        self.grid[row][col] = num
                        return False
                    self.grid[row][col] = num
        return True
