import pytest
from solver_sudoku import SolveSudoku


@pytest.fixture
def solver():
    return SolveSudoku()


def test_set_cell(solver):
    solver.set_cell(0, 0, 5)
    assert solver.grid[0][0] == 5


def test_reset_grid(solver):
    solver.set_cell(0, 0, 5)
    solver.reset_grid()
    assert solver.grid == [[0] * 9 for _ in range(9)]


def test_find_empty_cell(solver):
    solver.set_cell(0, 0, 5)
    assert solver.find_empty_cell() == (0, 1)


def test_is_valid(solver):
    solver.set_cell(0, 0, 5)
    assert not solver.is_valid(5, 0, 1)
    assert solver.is_valid(3, 0, 1)


def test_is_valid_grid(solver):
    solver.set_cell(0, 0, 5)
    assert solver.is_valid_grid()
    solver.set_cell(0, 1, 5)
    assert not solver.is_valid_grid()


def test_solve(solver):
    puzzle = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    for r in range(9):
        for c in range(9):
            solver.set_cell(r, c, puzzle[r][c])
    assert solver.solve()
    assert solver.is_valid_grid()
