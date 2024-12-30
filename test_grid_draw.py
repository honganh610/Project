import pytest
import pygame
from grid_draw import GridDraw

@pytest.fixture
def grid_draw():
    pygame.font.init()
    game_font = pygame.font.Font(None, 36)
    cell_size = 40
    num_x_offset = 10
    num_y_offset = 10
    line_coordinates = [((0, 0), (100, 100)), ((100, 0), (0, 100)), ((50, 0), (50, 100))]
    return GridDraw(game_font, cell_size, num_x_offset, num_y_offset, line_coordinates)

def test_draw_lines(grid_draw):
    pygame.init()
    surface = pygame.Surface((200, 200))
    grid_draw.draw_lines(pygame, surface)
    # Check if lines are drawn correctly
    assert surface.get_at((50, 50)) == (0, 0, 255, 255)  # Blue line
    assert surface.get_at((25, 25)) == (173, 216, 230, 255)  # Light blue line


def test_draw_numbers(grid_draw):
    pygame.init()
    surface = pygame.Surface((300, 300))  # Tạo bề mặt lớn hơn để kiểm tra
    grid = [
        [1, 2, 3],
        [4, 0, 6],
        [7, 8, 9]
    ]
    test_grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    occupied_cells = {(0, 0), (2, 2)}

    grid_draw.draw_numbers(surface, grid, test_grid, occupied_cells)

    # Lấy font để kiểm tra
    font = grid_draw.game_font

    # Kiểm tra số 1 (đã có sẵn trong occupied_cells, nên màu đen)
    text_surface_1 = font.render("1", True, (0, 0, 0))
    assert surface.get_at((50, 50)) == text_surface_1.get_at((5, 5))

    # Kiểm tra số 5 (sai, nên màu đỏ)
    text_surface_5 = font.render("5", True, (255, 0, 0))
    assert surface.get_at((150, 150)) == text_surface_5.get_at((5, 5))

    # Kiểm tra số 9 (đúng, nên màu xanh)
    text_surface_9 = font.render("9", True, (0, 255, 0))
    assert surface.get_at((250, 250)) == text_surface_9.get_at((5, 5))
