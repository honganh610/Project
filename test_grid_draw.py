import pygame
import pytest
from grid_draw import GridDraw

# Fixture để thiết lập môi trường pygame
@pytest.fixture
def setup_pygame_environment():
    pygame.init()
    screen = pygame.display.set_mode((1200, 900))
    game_font = pygame.font.SysFont('Comic Sans MS', 50)
    cell_size = 100
    num_x_offset = 35
    num_y_offset = 35
    line_coordinates = [
        ((0, 0), (900, 0)), ((0, 100), (900, 100)), ((0, 200), (900, 200)),
        ((0, 300), (900, 300)), ((0, 400), (900, 400)), ((0, 500), (900, 500)),
        ((0, 600), (900, 600)), ((0, 700), (900, 700)), ((0, 800), (900, 800)),
    ]
    return pygame, screen, game_font, cell_size, num_x_offset, num_y_offset, line_coordinates


# Kiểm tra chức năng vẽ các dòng
def test_draw_lines(setup_pygame_environment):
    pygame, screen, game_font, cell_size, num_x_offset, num_y_offset, line_coordinates = setup_pygame_environment
    grid_draw = GridDraw(game_font, cell_size, num_x_offset, num_y_offset, line_coordinates)

    surface = pygame.Surface((1200, 900))  # Tạo một surface để vẽ
    grid_draw.draw_lines(pygame, surface)

    for line_index, points in enumerate(line_coordinates):
        if line_index in {2, 5, 10, 13}:  # Dòng màu xanh
            color = surface.get_at(points[0])
            assert color == (0, 0, 255, 255), f"Dòng {line_index} phải có màu xanh, nhưng có màu {color}"
        else:  # Dòng màu xanh nhạt
            color = surface.get_at(points[0])
            assert color == (173, 216, 230, 255), f"Dòng {line_index} phải có màu xanh nhạt, nhưng có màu {color}"


# Kiểm tra chức năng vẽ các số
def test_draw_numbers(setup_pygame_environment):
    pygame, screen, game_font, cell_size, num_x_offset, num_y_offset, line_coordinates = setup_pygame_environment
    grid_draw = GridDraw(game_font, cell_size, num_x_offset, num_y_offset, line_coordinates)

    # Lưới mẫu
    grid = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
    ]

    # Lưới kiểm tra (có sự sai lệch để kiểm tra màu sắc sai)
    test_grid = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 2, 0, 1, 9, 5, 0, 0, 0],  # Lỗi cố ý để kiểm tra
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
    ]

    # Các ô đã điền (cần vẽ với màu đen)
    occupied_cells = [(0, 0), (0, 1), (1, 0)]

    # Tạo một surface để vẽ
    surface = pygame.Surface((1200, 900))
    grid_draw.draw_numbers(surface, grid, test_grid, occupied_cells)

    def color_is_close(actual, expected, tolerance=10):
        return all(abs(a - e) <= tolerance for a, e in zip(actual, expected))

    # Kiểm tra màu sắc của các số
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            # Vị trí của số trên surface
            center_x = num_x_offset + x * cell_size + cell_size // 2
            center_y = num_y_offset + y * cell_size + cell_size // 2

            # Lấy màu của số tại vị trí đó (lấy từ góc trái của ô thay vì giữa)
            color = surface.get_at((num_x_offset + x * cell_size, num_y_offset + y * cell_size))

            # Kiểm tra màu sắc của ô đã điền
            if (y, x) in occupied_cells:
                assert color_is_close(color, (10, 10, 10, 255))

            # Kiểm tra màu sắc của ô sai
            elif grid[y][x] != test_grid[y][x]:
                assert color_is_close(color, (255, 0, 0, 255))

            # Kiểm tra màu sắc của ô đúng
            elif grid[y][x] != 0:  # Nếu ô có số và không bị sai
                assert color_is_close(color, (0, 255, 0, 255))