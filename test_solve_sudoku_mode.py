import pytest
import pygame
from unittest.mock import patch
from grid_draw import GridDraw
from solver_sudoku import SolveSudoku
from utils import create_line_coordinates


def test_create_line_coordinates():
    cell_size = 100
    expected_lines = [[(0, i * cell_size),
                       (900, i * cell_size)]for i in range(1, 9)] + \
                     [[(i * cell_size, 0), (i * cell_size, 900)]
                      for i in range(1, 10)]
    assert create_line_coordinates(cell_size) == expected_lines


def test_solve_sudoku():
    solver = SolveSudoku()
    solver.grid = [
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
    assert solver.solve() is True
    assert solver.is_valid_grid() is True

    # Mock backtracking for unsolvable grid
    with patch.object(solver, "solve", return_value=False) as mock_solve:
        solver.grid[0][0] = 9  # Conflict
        assert solver.is_valid_grid() is False
        assert solver.solve() is False
        mock_solve.assert_called_once()


def test_grid_draw():
    pygame.font.init()
    font = pygame.font.Font(None, 36)
    grid_draw = GridDraw(
        game_font=font,
        cell_size=100,
        num_x_offset=35,
        num_y_offset=35,
        line_coordinates=create_line_coordinates(100)
    )
    assert grid_draw.cell_size == 100
    assert grid_draw.num_x_offset == 35
    assert grid_draw.num_y_offset == 35
    pygame.font.quit()


@pytest.fixture
def mock_pygame():
    pygame.init()
    screen = pygame.display.set_mode((900, 900))
    font = pygame.font.Font(None, 36)
    yield pygame, screen, font
    pygame.quit()


def test_solve_sudoku_mode(mock_pygame):
    _, _, font = mock_pygame
    # Initialize components
    _ = GridDraw(
        game_font=font,
        cell_size=100,
        num_x_offset=35,
        num_y_offset=35,
        line_coordinates=create_line_coordinates(100)
    )
    solver = SolveSudoku()

    # Create a test grid
    grid = [[0 for _ in range(9)] for _ in range(9)]
    grid[0][0] = 5

    # Simulate solving
    solver.grid = grid
    assert solver.is_valid_grid() is True
    assert solver.solve() is True

    # Test for unsolvable scenario with mocked solve method
    with patch.object(solver, "solve", return_value=False) as mock_solve:
        grid[0][0] = 9  # Introduce a conflict
        solver.grid = grid
        assert solver.is_valid_grid() is False
        assert not solver.solve()
        mock_solve.assert_called_once()
