import pytest
from utils import create_line_coordinates, pattern, shuffle, create_grid, remove_numbers, GRID_SIZE, SUB_GRID_SIZE

def test_create_line_coordinates():
    cell_size = 100
    points = create_line_coordinates(cell_size)
    assert len(points) == 17  # 8 horizontal + 9 vertical lines
    assert points[0] == [(0, 100), (900, 100)]
    assert points[8] == [(100, 0), (100, 900)]
    assert points[-1] == [(900, 0), (900, 900)]

def test_pattern():
    assert pattern(0, 0) == 0
    assert pattern(0, 1) == 1
    assert pattern(1, 1) == 4
    assert pattern(2, 2) == 8

def test_shuffle():
    samp = range(9)
    shuffled = shuffle(samp)
    assert sorted(shuffled) == list(samp)
    assert len(shuffled) == len(samp)

def test_create_grid():
    grid = create_grid(SUB_GRID_SIZE)
    assert len(grid) == 9
    assert all(len(row) == 9 for row in grid)

    for row in grid:
        assert sorted(row) == list(range(1, 10))

    for col_idx in range(9):
        col = [grid[row_idx][col_idx] for row_idx in range(9)]
        assert sorted(col) == list(range(1, 10))

    for box_row in range(3):
        for box_col in range(3):
            subgrid = [
                grid[r][c]
                for r in range(box_row * 3, (box_row + 1) * 3)
                for c in range(box_col * 3, (box_col + 1) * 3)
            ]
            assert sorted(subgrid) == list(range(1, 10))

def test_remove_numbers():
    grid = create_grid(SUB_GRID_SIZE)
    remove_numbers(grid)

    assert len(grid) == 9
    assert all(len(row) == 9 for row in grid)

    empty_count = sum(1 for row in grid for value in row if value == 0)
    non_empty_count = sum(1 for row in grid for value in row if value != 0)
    assert empty_count > 0
    assert non_empty_count + empty_count == 81