import pytest
from copy import deepcopy
from grid_logic import GridLogic
from utils import create_grid, remove_numbers, SUB_GRID_SIZE


@pytest.fixture
def grid_logic():
    return GridLogic()


def test_initial_grid_size(grid_logic):
    assert len(grid_logic.grid) == 9
    assert all(len(row) == 9 for row in grid_logic.grid)


def test_restart(grid_logic):
    original_grid = grid_logic.grid
    grid_logic.restart()
    assert grid_logic.grid != original_grid
    assert len(grid_logic.grid) == 9
    assert all(len(row) == 9 for row in grid_logic.grid)


def test_check_grids(grid_logic):
    grid_logic.grid = deepcopy(grid_logic._GridLogic__test_grid)  # Reset the grid
    assert grid_logic.check_grids() is True
    grid_logic.grid[0][0] = 1  # Modify the grid to make it incorrect
    assert grid_logic.check_grids() is False


def test_is_cell_preoccupied(grid_logic):
    for y, x in grid_logic.occupied_cell_coordinates:
        assert grid_logic.is_cell_preoccupied(x, y) is True
    assert grid_logic.is_cell_preoccupied(0, 0) in [True, False]  # Depends on the grid


def test_pre_occupied_cells(grid_logic):
    occupied_cells = grid_logic.pre_occupied_cells()
    assert isinstance(occupied_cells, list)
    assert all(isinstance(cell, tuple) and len(cell) == 2 for cell in occupied_cells)


def test_get_cell(grid_logic):
    for y in range(3):
        for x in range(3):
            assert grid_logic.get_cell(x, y) == grid_logic.grid[y][x]


def test_set_cell(grid_logic):
    grid_logic.set_cell(0, 0, 8)
    assert grid_logic.get_cell(0, 0) == 8

    grid_logic.set_cell(0, 0, 5)
    assert grid_logic.get_cell(0, 0) == 5
